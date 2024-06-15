from setuptools import setup, find_packages

setup(
    name='solved.py',
    version='0.2.0',
    description='solved.ac api wrapper for python',
    author='cywohoy',
    author_email='papertoy1127@gmail.com',
    url='https://github.com/papertoy1127/solved.py',
    install_requires=['aiohttp'],
    packages=find_packages(exclude=[]),
    keywords=[],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)
