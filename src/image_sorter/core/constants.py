import pathlib
from os.path import join

ROOT_DIR = pathlib.Path(pathlib.Path(__file__).parents[3])
IMAGE_DIR = join(ROOT_DIR, "images")
print(IMAGE_DIR)
