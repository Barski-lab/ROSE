from setuptools import setup, find_packages
import os

setup(
    name='rose',
    description='ROSE: rank ordering of super-enhancers',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    version='0.0.1',
    url='http://younglab.wi.mit.edu/super_enhancer_code.html',
    download_url=('https://github.com/Barski-lab/ROSE'),
    author='Michael Kotliar',
    author_email='misha.kotliar@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'rose': ['ROSE_callSuper.R']},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "ROSE=rose.ROSE_main:main"
        ]
    }
)