import logging
from pathlib import Path
from typing import List

import requests

from .dataclasses import Dependency, Semver
from .errors import NeedsHumanAttention
from .tomlfile import TOMLFile

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Pipfile:
    def __init__(self, dry_run: bool, directory: Path, ignored_packages: List[str]):
        self.pipfile_path: Path = directory / "Pipfile"
        self.pipfile: TOMLFile = TOMLFile(filepath=self.pipfile_path)

        self.dependencies: List[Dependency] = []

        self.process_packages(path="packages", ignored_packages=ignored_packages)
        self.process_packages(path="dev-packages", ignored_packages=ignored_packages)

        self.log_dependency_updates()

        if not dry_run:
            self.update_pipfile_dependencies()
            self.pipfile.save_file()

    def get_latest_version(self, package: str) -> str:
        response = requests.get(f"https://pypi.org/pypi/{package}/json")
        json_response = response.json()

        return str(json_response["info"]["version"])

    def process_packages(self, path: str, ignored_packages: List[str]) -> None:
        for pkg_name, pkg_version in self.pipfile.toml_data[path].items():
            if pkg_name in ignored_packages:
                continue

            try:
                self.dependencies.append(
                    Dependency(
                        dependency_type=path,
                        package=pkg_name,
                        current_version=Semver(version=pkg_version),
                        latest_version=Semver(
                            version=self.get_latest_version(package=pkg_name)
                        ),
                    )
                )
            except NeedsHumanAttention as err:
                logging.warning(
                    f"Package: {pkg_name} could not be updated to latest version. Reason: {err}"
                )

    def update_pipfile_dependencies(self) -> None:
        for dependency in self.dependencies:
            package: str = dependency.package
            new_version: str = dependency.latest_version_with_constraints

            if package in self.pipfile.toml_data["packages"].keys():
                self.pipfile.toml_data["packages"][package] = new_version
            if package in self.pipfile.toml_data["dev-packages"].keys():
                self.pipfile.toml_data["dev-packages"][package] = new_version

    def log_dependency_updates(self) -> None:
        for dependency in self.dependencies:
            if (
                dependency.current_version.version
                != dependency.latest_version_with_constraints
            ):
                logging.info(dependency)
