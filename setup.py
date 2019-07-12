import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="New Relic Synthetics API Wrapper",
    version="0.0.1",
    author="David Michael",
    author_email="1.david.michael@gmail.com",
    description="A higher-level wrapper around the New Relic Synthetics API.",
    url="https://github.com/1davidmichael/new-relic-synthetics-wrapper-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
