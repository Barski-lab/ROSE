from setuptools import setup, find_packages
import os

setup(
    name='ROSE',
    description='ROSE: RANK ORDERING OF SUPER-ENHANCERS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    version='0.0.1',
    url='http://younglab.wi.mit.edu/super_enhancer_code.html',
    download_url=('https://github.com/Barski-lab/ROSE'),
    author='Michael Kotliar',
    author_email='misha.kotliar@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "ROSE=rose.ROSE_main:main"
        ]
    }
)