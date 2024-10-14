from setuptools import setup, find_packages

setup(
    name='pyhepcommon',
    version='0.0.1',
    url='https://github.com/nVentis/pyhepcommon',
    author='Bryan Bliewert',
    author_email='bryan.bliewert@nventis.eu',
    description='Collection of classes and functions for HEP analysis',
    packages=find_packages(),    
    install_requires=[
        'numpy >= 1.24.3',
        'matplotlib >= 3.7.2',
        'luigi >= 3.5.1',
        'pandas >= 2.0.3',
        'scipy >= 1.11.1',
        'seaborn >= 0.12.2',
        'law@git+https://github.com/riga/law#673c2ac16eb8da9304a6c749e557f9c42ad4d976'
    ],
)