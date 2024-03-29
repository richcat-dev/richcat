import setuptools
from os import path
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = 'richcat'
main_directory = 'richcat'
root_dir = path.abspath(path.dirname(__file__))

def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

with open(path.join(root_dir, main_directory, '__information__.py')) as f:
    init_text = f.read()
    _version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    _license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    _author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    _author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    _url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert _version
assert _license
assert _author
assert _author_email
assert _url

setuptools.setup(
    name=package_name,
    version=_version,
    author=_author,
    author_email=_author_email,
    description="rich cat command working on Python",
    long_description=long_description,
    keywords='cat, rich',
    long_description_content_type="text/markdown",
    url=_url,
    packages=setuptools.find_packages(),
    install_requires=_requirements(),
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    license=_license,
    entry_points = {
        'console_scripts': [
            'richcat = richcat.richcat:main',
            ],
        },
    python_requires='>=3.6',
)
