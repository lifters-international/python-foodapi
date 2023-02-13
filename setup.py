import pathlib
from setuptools import *

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pythonFoodApi",
    version="1.0.1",
    description="Python wrapper for the Lifters Food API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lifters-international/python-foodapi",
    project_urls={
      "Bug Tracker": "https://github.com/lifters-international/python-foodapi/issues",
    },
    author="Lifters International",
    author_email="codingwithcn@gmail.com",
    license="MIT",
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = ["requests"],
    include_package_data = True,
    zip_safe = False,
)