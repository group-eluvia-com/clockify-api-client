from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify-api-client',  # Required
    version='0.5.0',  # Required
    author="Michael Bláha",
    author_email="michael.blaha@eluvia.com",
    description="Simple python API client for clockify.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.spkapps.eu/libraries/python/clockify-api-client",
    packages=find_packages(),

    install_requires=[
        'requests', 'factory_boy'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['wheel'],
)
