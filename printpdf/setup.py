from setuptools import setup, find_packages

VERSION = "0.1.1"

setup(
    name="printpdf",
    version=VERSION,
    package_dir={"printpdf": "SRC"},
    packages=[package.replace("SRC", "printpdf") for package in find_packages()],
    install_requires=[requirement for requirement in open("requirements.txt", "r")],
    entry_points={
        "console_scripts": [
            "printpdf = printpdf.main:main"
        ]
    }
)