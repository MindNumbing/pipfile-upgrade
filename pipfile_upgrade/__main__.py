from argparse import ArgumentParser
from pathlib import Path

from pipfile_upgrade.pipfile import Pipfile


def dir_path(input: str) -> Path:
    path = Path(input)
    if path.is_dir():
        return path
    else:
        raise NotADirectoryError(input)


def main() -> None:
    argument_parser = ArgumentParser(
        prog="pipfile_upgrade", usage="Upgrades your outdated pipfile packages"
    )

    argument_parser.add_argument(
        "--path",
        type=dir_path,
        dest="path",
        default=Path.cwd(),
        help="path where pipfile exists",
    )
    argument_parser.add_argument(
        "-d",
        "--dry",
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="only print outdated package updates",
    )
    argument_parser.add_argument(
        "ignored_packages",
        metavar="package_blocklist",
        type=str,
        nargs="*",
        help="list of packages to be ignored",
    )

    options = argument_parser.parse_args()

    Pipfile(dry_run=options.dry_run, directory=options.path, ignored_packages=options.ignored_packages)


if __name__ == "__main__":
    main()
