import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# This call to setup() does all the work
setup(
    name="dizge",
    version="0.1.4",
    description="The OOP based grammar analyzer for Turkish",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/mehmetumutmutlu/dizge",
    author="Mehmet Umut Mutlu, Nazlıcan Yetimaslan, İlker Atagün",
    author_email="mehmetumutmutlu@gmail.com",
    license="MIT",
    keywords=['python', 'nlp', 'linguistics', 'phonology', "turkish", "grammar"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
    ]
)