

from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='YassaAlchemy',
  version='0.0.1',
  description='Another MySQL based ORM',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Yassa Taiseer',
  author_email='yassataiseer@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='MySQL ORM Python', 
  packages=find_packages(),
  install_requires=[''] 
)