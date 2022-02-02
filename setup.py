from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in unicase_ecom/__init__.py
from unicase_ecom import __version__ as version

setup(
	name="unicase_ecom",
	version=version,
	description="Ecommerce Site",
	author="Mangal",
	author_email="rock.team.381@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
