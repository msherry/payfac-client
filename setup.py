#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup
setup(name='payfac',
      version='0.0.1',
      description="Python client for Litle's Payfac API",
      author='Marc Sherry',
      author_email='marc@balancedpayments.com',
      url='http://www.balancedpayments.com',
      packages=['payfac'],
      install_requires=[
          'PyXB>=1.2.3',
          'requests',
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Environment :: MacOS X'
          'Environment :: Plugins'
          'Environment :: Win32 (MS Windows)'
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Office/Business :: Financial',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      )
