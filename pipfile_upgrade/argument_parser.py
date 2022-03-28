from argparse import ArgumentParser
from pathlib import Path

from pipfile_upgrade.errors import InvalidDirectoryError, MissingPipfileError


class Parser:
    def __init__(self) -> None:
        self.parser = ArgumentParser(prog="pipfile_upgrade", usage="Upgrades your outdated pipfile packages")

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
        command_group = self.parser.add_mutually_exclusive_group()
        command_group.add_argument(
            "-required", dest="only_required", help="only upgrade required packages", action="store_true"
        )
        command_group.add_argument("-dev", dest="only_dev", help="only upgrade dev packages", action="store_true")

    @staticmethod
    def dir_path(input: str) -> Path:
        path: Path = Path(input)
        if path.is_dir():
            pipfile_path = path / "Pipfile"
            if pipfile_path.is_file():
                return pipfile_path
            else:
                raise MissingPipfileError(
                    f"{pipfile_path} does not exist. Please provide a path that contains a Pipfile."
                )
        else:
            raise InvalidDirectoryError(f"{input} is not a valid directory path.")
