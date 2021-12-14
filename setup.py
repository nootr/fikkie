from fikkie.version import VERSION
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='fikkie',
    version=VERSION,
    description='A simple remote service watchdog.',
    license='MIT',
    long_description=long_description,
    author='Joris Hartog (@nootr)',
    long_description_content_type='text/markdown',
    scripts=['scripts/fikkie'],
    install_requires=[
        'celery==5.2.1',
        'python-telegram-bot==13.9',
        'PyYAML==6.0',
        'tinydb==4.5.2',
    ],
)
