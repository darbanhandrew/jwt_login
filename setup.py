from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jwt_login/__init__.py
from jwt_login import __version__ as version

setup(
	name="jwt_login",
	version=version,
	description="Jwt ogin",
	author="Mohammad Darban Baran",
	author_email="darbanhandrew@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
