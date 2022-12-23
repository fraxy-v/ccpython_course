# Rename files of type in directory
from pathlib import Path

for filepath in Path().glob("*.gjf"):
    filepath.rename(filepath.with_suffix(".txt"))
