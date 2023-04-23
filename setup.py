from setuptools import setup

import os


if __name__ == '__main__':
    setup(
        name='m3_project',
        version=os.getenv('PACKAGE_VERSION', '1.0.0')
    )
