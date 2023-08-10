from setuptools import setup
from pathlib import Path
from genoml import __version__

# Use pathlib to get the current file's directory
base_dir = Path(__file__).parent

# Read the contents of README.md and requirements.txt
with (base_dir / "README.md").open("r") as fp:
    long_description = fp.read()

with (base_dir / "requirements.txt").open("r") as fp:
    requirements = fp.read().splitlines()

setup(
    name='genoml',
    version=__version__,
    packages=['genoml', 'genoml.steps'],
    url='https://github.com/genoml/genoml-core',
    license='Apache-2.0',
    author='Sayed Hadi Hashemi',
    author_email='SayedHadiHashemi@gmail.com',
    maintainer='Faraz Faghri',
    maintainer_email='faraz.faghri@gmail.com',
    description='Machine Learning for Genomic',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    entry_points={
        'console_scripts': [
            'genoml-cli=genoml.main:cli',
            'genoml-train=genoml.main:train',
            'genoml-inference=genoml.main:inference',
        ],
    },
    install_requires=requirements,
    package_data={'genoml': ['misc/*', 'misc/*/*', 'experimental/*', 'experimental/*/*']},
)

