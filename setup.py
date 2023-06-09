from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nextash/__init__.py
from nextash import __version__ as version

setup(
	name="nextash",
	version=version,
	description="nextash",
	author="nextash",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
