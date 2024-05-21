import sys
from pathlib import Path

def __add_path():
    curr_dir_path: Path = Path(__file__).absolute().parent
    root_dir_path: Path = curr_dir_path.parent.parent
    if str(root_dir_path) not in sys.path:
        sys.path.insert(0, str(root_dir_path))

__add_path()