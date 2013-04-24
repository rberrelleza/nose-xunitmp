import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import setup

setup(
    name='xunit multiprocess',
    version='0.1',
    author='Ramiro Berrelleza',
    author_email = 'rberrelleza@gmail.com',
    description = 'xunit reports with multiprocess support',
    py_modules = ['xunitmultiprocess'],
    entry_points = {
        'nose.plugins': [
            'xunitmultiprocess = xunitmultiprocess:Xunitmp'
            ]
        }
    )