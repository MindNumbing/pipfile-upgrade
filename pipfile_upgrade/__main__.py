from pipfile_upgrade.argument_parser import Parser
from pipfile_upgrade.pipfile import Pipfile


def main() -> None:
    options = Parser().parser.parse_args()

    Pipfile(
        dry_run=options.dry_run,
        directory=options.path,
        ignored_packages=options.ignored_packages,
        only_required=options.only_required,
        only_dev=options.only_dev,
    )


if __name__ == "__main__":
    main()
