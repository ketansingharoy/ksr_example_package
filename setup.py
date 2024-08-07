from setuptools import setup, find_packages

setup(
    name='ksr_example_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'numpy'
    ],
    include_package_data=True,
    description='An example Python project',
    author='Ketan Singha Roy',
    author_email='ketansingharoy@gmail.com',
    url='https://github.com/ketansingharoy/example_package.git',  # Update with your URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
