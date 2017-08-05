"""setup tools control"""

from setuptools import setup

version = '0.0.1'
reqs = ['numpy']

setup(
    name='debt-balance',
    packages=['balancer', 'test', 'cli'],
    setup_requires=['flake8'],
    test_suite='test',
    entry_points={
        "console_scripts": ['payment-balance = cli.cli:main']
        },
    version=version,
    description="A tool for evenly sharing the costs of a trip.",
    long_description="A tool for evenly sharing the costs of a trip",
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Development Status :: 1 - Planning',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: End Users/Desktop',
      'License :: Other/Proprietary License',
      'Programming Language :: Python :: 3 :: Only',
      'Topic :: Utilities'
     ],
    keyword='money vacation trip finance',
    license='MIT',
    install_requires=reqs,
    author="Luke Duncan",
    author_email="lukejduncan@gmail.com",
    url='http://www.lukejduncan.com',
    )
