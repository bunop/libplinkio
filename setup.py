from setuptools import setup, Extension
import os
import glob
import sys

libplinkio_src_dir = "src"
libplinkio_include_dir = libplinkio_src_dir
libplinkio_src_files = glob.glob(os.path.join(libplinkio_src_dir, "*.c"))

pyplinkio_src_dir = "py-plinkio/src/cplinkio"
pyplinkio_include_dir = pyplinkio_src_dir
pyplinkio_src_files = glob.glob(os.path.join(pyplinkio_src_dir, "*.c"))

libraries = []
if sys.platform == 'win32':
    libraries.append("Bcrypt")

cplinkio = Extension(
    "plinkio.cplinkio",
    libplinkio_src_files + pyplinkio_src_files,
    library_dirs=[],
    include_dirs=[
        libplinkio_include_dir,
        pyplinkio_include_dir,
    ],
    libraries=libraries,
    language="c",
    extra_compile_args=[],
    define_macros=[],
)

setup(
    name="plinkio",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.9.9.dev0",
    description="A library for parsing plink genotype files",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/mfranberg/libplinkio",
    # Author details
    author="Mattias Franberg",
    author_email="mattias.franberg@gmail.com",
    # Choose your license
    license="BSD",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: BSD License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    # What does your project relate to?
    keywords="plinkio bioinformatics genetics",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages("py-plinkio"),
    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={},
    ext_modules=[cplinkio],
)
