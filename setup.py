from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fikkie",
    version="0.3.3",
    description="Lightweight monitoring tool",
    license="MIT",
    long_description=long_description,
    author="Joris Hartog (@nootr)",
    long_description_content_type="text/markdown",
    url="https://nootr.github.io/fikkie/",
    packages=["fikkie", "fikkie.notifiers"],
    scripts=["scripts/fikkie"],
    install_requires=[
        "celery==5.2.1",
        "PyYAML==6.0",
        "tinydb==4.5.2",
        "typing_extensions==4.0.1",
    ],
)
