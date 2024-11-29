from setuptools import setup

setup(name='marga_pulseq',
      version='0.2.1',
      description='A simple interpreter from PulSeq 1.4 to MARGA',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/marcos-mri/marga_pulseq',
      author='Lincoln Craven-Brightman,'
             'Benjamin Menkuec,'
             'José Miguel Algarín',
      author_email='lcraven-brightman@mgh.harvard.edu,'
                   'benjamin.menkuec@fh-dortmund.de'
                   'josalggui@i3m.upv.es',
      license='MIT',
      packages=['marga_pulseq'],
      install_requires=[],
      classifiers=['Operating System :: OS Independent',
                   'Programming Language :: Python'],
      python_requires='>=3.6',
      )