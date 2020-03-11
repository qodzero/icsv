import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='icsv',
	version='0.1.6',
	scripts=['icsv/csv'],
	license='MIT',
	keywords=['csv'],
	author='Samuel Mtembo',
	author_email='samuel@samuelworks.org',
	description='A simple script to make operating csv files easier',
	long_description=long_description,
	url='https://www.samuelworks.org',
	download_url='https://github.com/qodzero/icsv/archive/v1.0.5.tar.gz',
	packages=setuptools.find_packages(),
	classifiers=[
			"Programming Language ::Python :: 3",
			"License :: OSI Approved :: MIT License",
			"operating System :: OS Independent",
		]
	)
