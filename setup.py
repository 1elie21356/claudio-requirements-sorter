from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as install_requirements_file:
    install_requirements = install_requirements_file.read().split()

with open("test_requirements.txt") as test_requirements_file:
    test_requirements = test_requirements_file.read().split()

setup(
    author="Elie",
    author_email='1elie21356@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description="Sort requirements file for python ",
    entry_points={
        'console_scripts': [
            'claudio_requirements_sorter=claudio_requirements_sorter.cli:main',
        ],
    },
    install_requires=install_requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='claudio_requirements_sorter',
    name='claudio_requirements_sorter',
    packages=find_packages(include=["claudio_requirements_sorter"]),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/1elie21356/claudio-sorter',
    version='0.4.0',
    zip_safe=False,
)
