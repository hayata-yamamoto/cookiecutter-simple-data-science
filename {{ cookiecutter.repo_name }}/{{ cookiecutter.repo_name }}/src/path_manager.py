from pathlib import Path
from typing import List


class PathManager:
    BASE_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_ROOT: Path = BASE_DIR / "data"
    PROJECT_ROOT: Path = BASE_DIR / "{{ cookiecutter.project_name }}"

    # data directory
    RAW_DIR: Path = DATA_ROOT / "raw"
    INTERIM_DIR: Path = DATA_ROOT / "interim"
    PROCESSED_DIR: Path = DATA_ROOT / "processed"

    # notebooks directory
    NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
    EXPLORATORY_DIR = NOTEBOOK_DIR / "exploratory"
    PREDICTIVE_DIR = NOTEBOOK_DIR / "predictive"

    # src directory
    SRC_ROOT = PROJECT_ROOT / "src"
    DATASETS_DIR = SRC_ROOT / "datasets"
    FEATURES_DIR = SRC_ROOT / "features"
    MODELS_DIR = SRC_ROOT / "models"
    TASKS_DIR = SRC_ROOT / "tasks"
    TESTS_DIR = SRC_ROOT / "tests"
    
    @staticmethod
    def get_data_dirs() -> List[Path]:
        return [PathManager.RAW_DIR, PathManager.INTERIM_DIR, PathManager.PROCESSED_DIR]

    @staticmethod
    def get_project_dirs() -> List[Path]:
        return [PathManager.NOTEBOOK_DIR, PathManager.SRC_ROOT, PathManager.DATASETS_DIR, PathManager.FEATURES_DIR,
                PathManager.MODELS_DIR, PathManager.TASKS_DIR, PathManager.TESTS_DIR]

