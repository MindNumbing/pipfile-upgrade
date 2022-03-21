from argparse import ArgumentParser
from pathlib import Path

class Parser:

    def __init__(self):
        self.parser = ArgumentParser(
            prog="pipfile_upgrade", usage="Upgrades your outdated pipfile packages"
        )

        self.parser.add_argument(
            "--path",
            type=self.dir_path,
            dest="path",
            default=Path.cwd(),
            help="path where pipfile exists",
        )
        self.parser.add_argument(
            "-d",
            "--dry",
            "--dry-run",
            dest="dry_run",
            action="store_true",
            help="only print outdated package updates",
        )
        self.parser.add_argument(
            "ignored_packages",
            metavar="package_blocklist",
            type=str,
            nargs="*",
            help="list of packages to be ignored",
        )
    
    def dir_path(input: str) -> Path:
        path = Path(input)
        if path.is_dir():
            return path
        else:
            raise NotADirectoryError(input)
