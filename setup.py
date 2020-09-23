from setuptools import setup, find_packages

import pdo

setup(
    name='pdo-pip',
    version=pdo.__version__,
    description='An interface to access a database from Python.',
    url='https://github.com/AlexisHuvier/PDO',
    author='AlexisHuvier',
    author_email='lavapower84@gmail.com',
    license='GNU GPLv3',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    install_requires=[],
    include_package_data=True,

    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Topic :: Database'
    ],
)