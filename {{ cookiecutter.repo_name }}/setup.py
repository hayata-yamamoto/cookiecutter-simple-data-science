from typing import NoReturn, IO

from setuptools import find_packages, setup


def main() -> NoReturn:

    f: IO
    with open('requirements.txt', 'r') as f:
        req = f.read().splitlines()

    setup(
        name="{{ cookiecutter.repo_name }}",
        author="{{ cookiecutter.author }}",
        version="{{ cookicutter.version }}",
        install_requires=req,
        packages=find_packages()
    )
if __name__ == '__main__':
    main()
