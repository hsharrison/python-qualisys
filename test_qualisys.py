import numpy as np
import pandas as pd

import qualisys


def test_metadata():
    assert qualisys.get_metadata('example_data.txt') == (
        {'no_of_cameras': 7,
         'data_included': '3D',
         'pc_on_time': 912.56663253,
         'no_of_analog': 0,
         'events': [],
         'description': '--',
         'frequency': 120,
         'analog_frequency': 0,
         'no_of_markers': 2,
         'no_of_frames': 720,
         'time_stamp': np.datetime64('2014-06-17T08:53:44-0400'),
         'marker_names': ['RIGHT_KNEE', 'right_ankle']},
        10)


def test_data():
    data, _ = qualisys.load_qtm_data('example_data.txt')

    assert set(data) == {'RIGHT_KNEE', 'right_ankle'}
    assert data.axes[1].dtype == 'float64'
    assert np.all(data.axes[2] == ['x', 'y', 'z'])

    for _, frame in data.iteritems():
        yield check_index, frame
        yield check_columns, frame


def test_multi_index():
    data, _ = qualisys.load_qtm_data('example_data.txt', multi_index=True)

    assert data.columns.identical(pd.MultiIndex.from_product(
        (['RIGHT_KNEE', 'right_ankle'], ['x', 'y', 'z']),
        names=['marker', 'dim']
    ))

    yield check_index, data
    yield check_columns, data


def test_datetime_index():
    data, _ = qualisys.load_qtm_data('example_data.txt', datetime_index=True)
    for _, frame in data.iteritems():
        yield check_datetime_index, frame


def test_datetime_index_multi_index():
    data, _ = qualisys.load_qtm_data('example_data.txt', multi_index=True, datetime_index=True)
    yield check_datetime_index, data


def check_datetime_index(frame):
    assert isinstance(frame.index, pd.DatetimeIndex)
    assert frame.index.name == 't'
    assert frame.index.dtype == 'datetime64[ns]'


def check_index(frame):
    assert isinstance(frame.index, pd.Float64Index)
    assert frame.index.name == 't'
    assert frame.index.dtype == 'float64'


def check_columns(frame):
    assert all(column.dtype == 'float64' for _, column in frame.items())
