===============
python-qualisys
===============

Load data from a .txt file exported from QTM into `pandas <http://pandas.pydata.org>`_::

    pip install qualisys

.. code-block:: python

    In [1]: from qualisys import load_qtm_data

    In [2]: data, metadata = load_qtm_data('example_data.txt')

    In [3]: metadata
    Out[3]:
    {'analog_frequency': 0,
     'description': '--',
     'events': [],
     'no_of_frames': 720,
     'pc_on_time': 912.56663253,
     'no_of_cameras': 7,
     'marker_names': ['right_knee', 'right_ankle'],
     'frequency': 120,
     'no_of_markers': 2,
     'no_of_analog': 0,
     'data_included': '3D',
     'time_stamp': numpy.datetime64('2014-06-17T08:53:44-0400')}

    In [4]: data.head()
    Out[4]:
                                   right_ankle                     right_knee  \
                                             x         y        z           x
    2014-06-17 12:53:44.008329999     1501.102  2073.985  102.815    1440.857
    2014-06-17 12:53:44.016669999     1501.187  2074.183  103.058    1440.625
    2014-06-17 12:53:44.025000        1501.052  2073.905  102.775    1434.826
    2014-06-17 12:53:44.033330        1501.557  2073.970  103.195    1435.092
    2014-06-17 12:53:44.041670        1501.425  2073.629  102.974    1435.118


                                          y        z
    2014-06-17 12:53:44.008329999  2052.804  474.694
    2014-06-17 12:53:44.016669999  2052.820  474.753
    2014-06-17 12:53:44.025000     2054.241  482.904
    2014-06-17 12:53:44.033330     2051.464  481.212
    2014-06-17 12:53:44.041670     2051.504  481.120
