from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fikkie",
    version="0.3.2",
    description="Lightweight monitoring tool",
    license="MIT",
    long_description=long_description,
    author="Joris Hartog (@nootr)",
    long_description_content_type="text/markdown",
    url="https://nootr.github.io/fikkie/",
    packages=["fikkie", "fikkie.notifiers"],
    scripts=["scripts/fikkie"],
    install_requires=[
        "celery",
        "PyYAML",
        "tinydb",
        "typing_extensions",
    ],
)
