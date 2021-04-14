import re
from setuptools import setup
from os import path

with open('represents/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

this_dir = path.abspath(path.dirname(__file__))

with open(path.join(this_dir, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='represents',
    packages=["represents"],
    version=version,
    license='MIT',
    description="A utility library to easily create __repr__'s.",
    project_urls={},
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Arthurdw',
    author_email='mail@arthurdw.com',
    url='https://github.com/Arthurdw/Represents',
    download_url=f'https://github.com/Arthurdw/Represents/archive/{version}.tar.gz',
    keywords=["__repr__", "repr", "represents"],
    install_requires=[],
    extras_require={},
    classifiers=[
        # Development statuses:
        "Development Status :: 5 - Production/Stable",
        # Development Status :: 6 - Mature
        # Development Status :: 7 - Inactive
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)