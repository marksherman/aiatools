#!/usr/bin/env python

from distutils.core import setup

setup(name='aiatools',
      version='p3-0.0.4',
      description='Tools for extracting information from App Inventor AIA files',
      author='Evan W. Patton',
      author_email='ewpatton@mit.edu',
      url='https://www.evanpatton.com/projects/aiatools/',
      packages=['aiatools'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Education',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Software Development',
          'Topic :: Utilities'
      ],
      license='GPLv3+',
      keywords='App Inventor AIA extraction analysis toolkit',
      entry_points={
          'console_scripts': [
              'aia = aiatools:aia_main'
          ]
      },
      install_requires=[
          'jprops>=2.0.2'
      ],
      package_data={
          'aiatools': ['simple_components.json']
      }
      )
