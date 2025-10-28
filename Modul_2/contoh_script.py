# contoh_script.py
# Small helper script for Modul_2: greet and list python files in the current folder.

from pathlib import Path
import argparse


def list_python_files(folder: str = ".") -> list:
    """Return a sorted list of .py filenames in the given folder."""
    p = Path(folder)
    return sorted([f.name for f in p.glob("*.py") if f.is_file()])


def greet(name: str = "Dosen") -> str:
    """Return a greeting string."""
    return f"Halo, {name}! Ini contoh script."


def main():
    parser = argparse.ArgumentParser(description="Contoh script: greet and list .py files in folder")
    parser.add_argument("--name", "-n", default="Suci", help="Name to greet")
    parser.add_argument("--folder", "-f", default=".", help="Folder to list .py files from")
    args = parser.parse_args()

    print(greet(args.name))
    print("\nPython files in folder:")
    for fn in list_python_files(args.folder):
        print("-", fn)


if __name__ == "__main__":
    main()
