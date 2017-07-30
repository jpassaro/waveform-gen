import os.path as osp
import re

from setuptools import setup

with open(osp.join(osp.dirname(__file__), 'waveform_gen', '__init__.py')) as v:
    VERSION = re.compile(r"\s*__version__\s*=\s*(['\"])(.*?)\1", re.S) \
        .match(v.read()).group(2)


setup(
    name='waveform-gen',
    version=VERSION,
    license='BSD',
    description='A mini-library to turn math functions to audio waveforms.',
    author='John Passaro',
    author_email='john.a.passaro@gmail.com',
    url='https://github.com/jpassaro/waveform-gen',
    packages=['waveform_gen'],
    entry_points={
        'console_scripts': [
            'wfgen=waveform_gen.cli:main',
        ]
    },
)
