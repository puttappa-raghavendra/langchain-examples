from setuptools import setup, find_packages

setup(
    name='langchain-examples',
    version='1.0.0',
    author='Raghavendra Puttappa',
    author_email='puttappa.raghavendra@gmail.com',
    description='Langchain Examples covering various core components',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add your project dependencies here
    ],
    classifiers=[
    ],
)