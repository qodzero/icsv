import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='icsv',
	version='0.1.4',
	scripts=['icsv/csv'],
	author='Samuel Mtembo',
	author_email='samuel@samuelworks.org',
	description='A simple script to make operating csv files easier',
	long_description=long_description,
	url='https://github.com/qodzero/icsv',
	packages=setuptools.find_packages(),
	classifiers=[
			"Programming Language ::Python :: 3",
			"License :: OSI Approved :: MIT License",
			"operating System :: OS Independent",
		]
	)
