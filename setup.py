from setuptools import setup, find_packages
import pathlib

base = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (base / "README.md").read_text(encoding="utf-8")

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  "Topic :: Software Development :: Libraries :: Python Modules",
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
]
 
setup(
  name='py_mongo_backup_restore',
  version='2.0.0',
  description='Python Library to Backup and Restore MongoDB',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/sannjayy/py-mongo-backup-restore',  
  author='Sanjay Sikdar',
  author_email='me@sanjaysikdar.dev',
  license='MIT', 
  classifiers=classifiers,
  keywords='python, mongo, backup, restore, mongodb', 
  packages=find_packages(where="src"),
  python_requires=">=3.10, <4",   
  package_dir={'':'src'},
  install_requires=[],
  project_urls={
    "Bug Reports": "https://github.com/sannjayy/py-mongo-backup-restore/issues",
    "Funding": "https://www.paypal.com/paypalme/znasofficial",
    "Say Thanks!": "https://saythanks.io/to/sannjayy",
    "Source": "https://github.com/sannjayy/py-mongo-backup-restore/",
  },
)