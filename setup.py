from setuptools import setup
from os.path import join, dirname


def read(*names, **kwargs):
    return open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')).read()


setup(
    name='python-qualisys',
    version='0.1.0',
    license='MIT',

    description='Import data from Qualisys Track Manager into pandas.',
    long_description=read('README.rst'),

    author='Henry S. Harrison',
    author_email='henry.schafer.harrison@gmail.com',

    url='https://bitbucket.org/hharrison/python-qualisys',
    download_url='https://bitbucket.org/hharrison/python-qualisys/get/default.tar.gz',

    py_modules=['qualisys'],

    keywords='qualisys qtm motion-capture import biomechanics',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Researchers',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering',
    ],

    install_requires=[
        'numpy',
        'pandas',
    ],
)