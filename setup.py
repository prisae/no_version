# -*- coding: utf-8 -*-
from setuptools import setup

description = 'A multigrid solver for 3D electromagnetic diffusion.'

setup(
    name='no_version',
    version='0.1.0',
    description='Package without __version__ number.',
    author='no_version',
    author_email='dieter@werthmuller.org',
    url='https://empymod.github.io',
    download_url='https://github.com/empymod/emg3d/tarball/v0.6.2',
    license='Apache License V2.0',
    packages=['emg3d'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'numpy>=1.15.0',
        'scipy>=1.1.0',
        'numba>=0.40.0',
        'scooby>=0.3.0'
    ],
)
