from collections import namedtuple

import numpy as np
import pandas as pd


QTMMetadata = namedtuple('QTMMetadata', ('metadata', 'n_lines'))
QTMData = namedtuple('QTMData', ('data', 'metadata'))
Event = namedtuple('Event', ('name', 'time'))


def get_metadata(file_path, sentinel_word='Frame'):
    """
    Load metadata from a .txt file generated by Qualisys Track Manager.

    Parameters
    ----------
    file_path : str
        Path to a .txt file.
    sentinel_word : str, optional
        Word indicating end of file header.

    Returns
    -------
    metadata : dict
    n_lines : int

    """
    with open(file_path, 'r') as f:
        metadata = {}
        raw_events = []
        n = 0
        for n, line in enumerate(f):
            label, *data = line.split()
            if label == sentinel_word:
                break

            if len(data) == 1:
                data = data[0]
            label = label.lower()

            if label == 'time_stamp':
                # The time_stamp field contains two pieces of metadata:
                # in addition to the time stamp, the time in seconds the pc has been on.
                metadata[label], metadata['pc_on_time'] = _parse_time_stamp(data)

            elif label == 'event':
                # We need the global time_stamp to process the event's time field.
                # So we process events later, in case we haven't encountered time_stamp yet.
                raw_events.append(data)

            elif label in (
                    'analog_frequency',
                    'frequency',
                    'no_of_analog',
                    'no_of_cameras',
                    'no_of_frames',
                    'no_of_markers',
            ):
                metadata[label] = int(data)

            else:
                metadata[label] = data

        # Now process events.
        metadata['events'] = [_parse_event(event, metadata['time_stamp']) for event in raw_events]

    return QTMMetadata(metadata, n)


def load_qtm_data(file_path, sentinel_word='Frame'):
    """
    Load data from a .txt file generated by Qualisys Track Manager.

    Parameters
    ----------
    file_path : str
        Path to a .txt file.
        Otherwise, collates the data in a Panel with one DataFrame per marker.
    sentinel_word : str, optional
        Word indicating end of file header.

    Returns
    -------
    data : pandas.DataFrame
    metadata : dict

    """
    metadata, n_lines = get_metadata(file_path, sentinel_word=sentinel_word)
    if metadata['data_included'] != '3D':
        raise TypeError('Only 3D data is supported')

    raw_data = pd.read_table(file_path, header=n_lines)

    data = pd.DataFrame({(marker, dim): raw_data[marker + ' ' + dim]
                         for dim in ('X', 'Y', 'Z')
                         for marker in metadata['marker_names']})
    data.columns = pd.MultiIndex.from_tuples(
        [(marker, dim.lower()) for marker, dim in data.columns])
    data.index = _create_time_index(raw_data['Time'], metadata['time_stamp'])

    return QTMData(data, metadata)


def _create_time_index(seconds, start_time):
    timedeltas = (10**9 * seconds).astype('timedelta64[ns]')
    return pd.DatetimeIndex(start_time + delta for delta in timedeltas)


def _parse_time_stamp(time_stamp):
    date = time_stamp[0].strip(',')
    time = time_stamp[1]
    return np.datetime64(date + 'T' + time), float(time_stamp[2])


def _parse_event(raw_event, start_time):
    name, frame, time = raw_event
    actual_time = np.timedelta64(int(10**9 * time), 'ns') + start_time
    # The frame number is redundant information, so we drop it.
    return Event(name, actual_time)
