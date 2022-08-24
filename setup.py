import os
import pathlib
from glob import glob

from setuptools import find_packages, setup

python_modules = [
    os.path.splitext(os.path.basename(path))[0]
    for path in glob(os.path.join("src", "*.py"))
]

setup(
    name="image-sorter",
    version=pathlib.Path("version.txt").read_text().strip(),
    author="David Valecký",
    author_email="d.valecky@gmail.com",
    install_requires=[
        "click",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    py_modules=python_modules,
    entry_points={"console_scripts": ["image-sorter = image_sorter.cli:cli"]},
)
