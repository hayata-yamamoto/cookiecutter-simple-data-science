from typing import NoReturn, IO

from setuptools import find_packages, setup


def main() -> NoReturn:

    f: IO
    with open('requirements.txt', 'r') as f:
        req = f.read().splitlines()

    setup(
        name="{{ cookiecutter.repo_name }}",
        description="{{ cookiecutter.description }}",
        version="0.1.0",
        install_requires=req,
        packages=find_packages(exclude=["data/", "notebooks"])
    )

if __name__ == '__main__':
    main()
