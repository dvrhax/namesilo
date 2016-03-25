import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='namesilo',
    version='0.2.0',
    url='http://github.com/dvrhax/namesilo',
    license='MIT',
    author='Dvr Hax',
    author_email='dvrhax@yahoo.com',
    description='A simple wrapper for the NameSilo API.',
    long_description=read('README.rst'),
    py_modules=['namesilo'],
    platforms='any',
    install_requires=['requests', 'untangle'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
