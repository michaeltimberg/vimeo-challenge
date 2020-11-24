from error_percentage import __version__ as version
from logging import exception
from setuptools import setup

try:
    with open('README.md', mode='r') as readme:
        long_description = readme.read()
except Exception as error:
    exception(msg=error)

setup(name='error_percentage',
      version=version,
      packages=['error_percentage'],
      url='none yet',
      license='none yet',
      author='Mike',
      author_email='timberg.1@osu.edu',
      description='Vimeo Challenge',
      long_description=long_description,
      long_description_content_type='text/markdown')
