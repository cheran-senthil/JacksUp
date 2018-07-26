from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(name='JacksUp',
      version='0.1.0',
      description='Poker API',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Cheran-Senthil/JacksUp',
      author='Cheran',
      license='MIT',
      packages=['jacksup'],
      install_requires=['Jacks'])
