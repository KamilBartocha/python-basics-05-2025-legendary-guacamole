from setuptools import setup, find_packages

setup(
    name="datareader",
    version="0.1.0",
    description="A library for reading and processing XML and JSON data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kamil Bartocha",
    author_email="kamilbartocha53@gmail.com",
    url="https://github.com/kamilbartocha/mydatareader",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)