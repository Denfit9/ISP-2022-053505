from setuptools import setup
"""Setup file"""

setup(name="JYTSerializer",
      version='1.0.0',
      description='This app contains JSON, Yaml and Toml serializers',
      author='Denfit9',
      url='https://github.com/Denfit9',
      requires=['TOML,YAML'],
      packages=['serializers,application'],
      scripts=['application/app_commands']
      )
