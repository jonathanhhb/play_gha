from setuptools import setup, Extension

setup(
    name='jhhb_bdist_test',
    version='1.0',
    packages=['jhhb_bdist_test'],
    ext_modules=[
        Extension('jhhb_bdist_test.my_extension', ['my_extension.c']),
    ],
    setup_requires=[
        'wheel',
        # Other dependencies
    ],
    install_requires=[
        'wheel',
        'twine',
        # Other dependencies
    ],
)

