"""Helper functions

"""

import logging
from pathlib import Path

FORMAT = '%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
logging.basicConfig(format=FORMAT, datefmt='%d/%m/%Y %H:%M:%S')
logger = logging.getLogger('default')
logger.setLevel(logging.INFO)

logger.setLevel(logging.ERROR)


def cast_path_into_pathlib(path_candidate):
    if isinstance(path_candidate, str):
        return Path(path_candidate)
    if isinstance(path_candidate, Path):
        return path_candidate
    raise ValueError(
        f'Un-recognized type for path_candidate argument: '
        f'{type(path_candidate)}. Expected str or pathlib.Path instance.')


def sanitize_path(path):
    return cast_path_into_pathlib(path).expanduser()


def log_and_exit(error_msg):
    logger.error(error_msg)
    exit(1)


def create_folder_if_needed(path: Path):
    if path.exists():
        return path
    path.mkdir(parents=True)
    return path
