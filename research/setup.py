"""Setup script for object_detection."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Pillow>=1.0', 'Matplotlib>=2.1', 'Cython>=0.28.1']

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=[p for p in find_packages() if p.startswith('object_detection')],
    package_data={'object_detection': ['data/*.pbtxt', 'protos/*.proto']},
    description='Tensorflow Object Detection Library',
)
