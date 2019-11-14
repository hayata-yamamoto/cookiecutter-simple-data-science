from pathlib import Path 
from dataclasses import dataclass

@dataclass(frozen=True)
class Const:
    pass


class PathManager: 
    ROOT_DIR = Path(__file__).resolve().parents[2]
    DATA_DIR = ROOT_DIR / "data"
    NOTEBOOK_DIR = ROOT_DIR / "notebooks"

    BASE_DIR = ROOT_DIR / "{{ cookiecutter.repo_name }}"

 
