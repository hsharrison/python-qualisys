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

    assert data.columns.identical(pd.MultiIndex.from_product(
        (['RIGHT_KNEE', 'right_ankle'], ['x', 'y', 'z']),
        names=['marker', 'dim']
    ))
    assert data.index.dtype == 'float64'
    assert data.index.name == 't'
    for _, column in data.iteritems():
        assert column.dtype == 'float64'


def test_datetime_index():
    data, _ = qualisys.load_qtm_data('example_data.txt', datetime_index=True)
    assert isinstance(data.index, pd.DatetimeIndex)
    assert data.index.dtype == 'datetime64[ns]'
    assert data.index.name == 't'
