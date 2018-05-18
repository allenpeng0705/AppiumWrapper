"""
EMA Appium Client
-----

EMA Appium Client is a microframework for EMA UI automation testing with/without one node.js mock backend

EMA Appium Client is Fun
```````````

"""
import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('EMAAppiumClient/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='EMAAppiumClient',
    version=version,
    url='https://www.everbridge.com/',
    license='BSD',
    author='Allen Peng',
    author_email='allen.peng@everbridge.com',
    description='A microframework for Everbridge mobile app UI automation testing',
    long_description=__doc__,
    packages=['EMAAppiumClient', 'EMAAppiumClient.json'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Appium-Python-Client',
    ],
    extras_require={
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
    '''
)
