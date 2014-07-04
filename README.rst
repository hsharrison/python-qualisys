===============
python-qualisys
===============

+--------------------+-------------------+
| | |travis-badge|   | | |version-badge| |
| | |coverage-badge| | | |license-badge| |
+--------------------+-------------------+

.. |travis-badge| image:: http://img.shields.io/travis/hsharrison/python-qualisys.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/hsharrison/python-qualisys
.. |coverage-badge| image:: http://img.shields.io/coveralls/hsharrison/python-qualisys.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/hsharrison/python-qualisys
.. |version-badge| image:: http://img.shields.io/pypi/v/python-qualisys.png?style=flat
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/python-qualisys
.. |license-badge| image:: http://img.shields.io/badge/license-MIT-blue.png?style=flat
    :alt: License
    :target: https://pypi.python.org/pypi/python-qualisys

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
     'marker_names': ['RIGHT_KNEE', 'right_ankle'],
     'frequency': 120,
     'no_of_markers': 2,
     'no_of_analog': 0,
     'data_included': '3D',
     'time_stamp': numpy.datetime64('2014-06-17T08:53:44-0400')}

    In [4]: data
    Out[4]:
    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 720 (major_axis) x 3 (minor_axis)
    Items axis: RIGHT_KNEE to right_ankle
    Major_axis axis: 0.00833 to 6.0
    Minor_axis axis: x to z

    In [5]: data['right_ankle'].head()
    Out[5]:
    dim             x         y        z
    t
    0.00833  1501.102  2073.985  102.815
    0.01667  1501.187  2074.183  103.058
    0.02500  1501.052  2073.905  102.775
    0.03333  1501.557  2073.970  103.195
    0.04167  1501.425  2073.629  102.974
