from setuptools import setup, Extension

setup(
    name='my_package',
    version='1.0',
    packages=['my_package'],
    ext_modules=[
        Extension('my_package.my_extension', ['my_extension.c']),
    ],
    setup_requires=[
        'wheel',
        # Other dependencies
    ],
    install_requires=[
        'wheel',
        # Other dependencies
    ],
)

