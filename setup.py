from setuptools import setup, find_packages

from breeze import __version__


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


requirements = parse_requirements('requirements.txt')

setup(
    name='breeze',
    version=__version__,
    url='https://github.com/chrisseto/breeze',
    packages=find_packages(exclude=("tests*", )),
    package_dir={'breeze': 'breeze'},
    include_package_data=True,
    # install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
