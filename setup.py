import os

from setuptools import find_packages, setup

from cli_gpt import __author__, __version__


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("cli-gpt", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split('\n')
        if not line.startswith(('#', 'git+', '"', '-'))
    ]


setup(
    name='cli-gpt',
    version=__version__,
    description='CLI with chatGPT',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author=__author__,
    python_requires='>=3.11',
    packages=find_packages(exclude=['integration']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gpt = cli_gpt.__main__:main'
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        'test': read_requirements('requirements.test.txt'),
        'dev': read_requirements("requirements.dev.txt")
    }
)
