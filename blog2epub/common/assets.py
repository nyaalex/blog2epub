import os
import subprocess
import sys


def asset_path(filename: str) -> str:
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath("./assets/")
    if os.path.isfile(os.path.join(base_path, filename)):
        return os.path.join(base_path, filename)
    # if there is no given file i'm guessing that blog2epub is run from sources
    return os.path.join(os.path.abspath("../assets/"), filename)


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
