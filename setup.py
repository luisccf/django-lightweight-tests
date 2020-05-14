import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-lightweight-tests',
    version='0.0.1',
    author='Luis Carlos Cardoso',
    author_email='luisccf@me.com',
    description='Run Django tests with optimization options to decrease runtime while keeping them trustable',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/luisccf/django-lightweight-tests',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
