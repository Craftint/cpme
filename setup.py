from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cpme/__init__.py
from cpme import __version__ as version

setup(
	name="cpme",
	version=version,
	description="CPME Customization",
	author="Happenize",
	author_email="info@happrnize",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
