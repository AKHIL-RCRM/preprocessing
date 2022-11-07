import setuptools

with open('README.md', 'r') as file:
    desc = file.read()

setuptools.setup(
    name = 'preprocess_akhil',
    version='0.0.1',
    author='AKHIL',
    author_email='akhilsmile20@gmail.com',
    description='This is prepocessing package',
    long_description=desc,
    long_description_content_type='text/markdown',
    packages=setuptools.file_packages(),
    classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'

)