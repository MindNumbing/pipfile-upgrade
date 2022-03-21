import logging
from pathlib import Path
from typing import List

from pipfile_upgrade.dataclasses import Pipfile_Dependencies
from pipfile_upgrade.tomlfile import TOMLFile

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Pipfile:
    def __init__(self, dry_run: bool, directory: Path, ignored_packages: List[str]):
        self.pipfile_path: Path = directory / "Pipfile"
        self.toml_file: TOMLFile = TOMLFile(filepath=self.pipfile_path)
        self.ignored_packages = ignored_packages

        self.pip_deps = Pipfile_Dependencies()
        self.pip_deps.load_toml_data(self.toml_file)

        self.log_dependency_updates()

        if not dry_run:
            self.update_pipfile_dependencies()
            self.toml_file.save_file()

    def update_pipfile_dependencies(self) -> None:
        for dependency in self.pip_deps.package_dependencies():
            if dependency.package not in self.ignored_packages:
                self.toml_file.toml_data["packages"][
                    dependency.package
                ] = dependency.latest_version_with_constraints
        for dependency in self.pip_deps.dev_package_dependencies():
            if dependency.package not in self.ignored_packages:
                self.toml_file.toml_data["dev-packages"][
                    dependency.package
                ] = dependency.latest_version_with_constraints

    def log_dependency_updates(self) -> None:
        for dependency in self.pip_deps.all_dependencies():
            if dependency.requires_update:
                logging.info(dependency)
