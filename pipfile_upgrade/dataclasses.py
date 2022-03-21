import re
import requests
from dataclasses import dataclass, field
from typing import List

from packaging.version import Version, parse

from pipfile_upgrade.tomlfile import TOMLFile


@dataclass
class Dependency:
    package: str
    current_version: str

    def __repr__(self) -> str:
        return f"Package: {self.package} {'is not' if self.requires_update else 'is'} up to date. Current version: {self.current_version}. Latest_version: {self.latest_version_with_constraints}"

    @property
    def latest_version(self):
        response = requests.get(f"https://pypi.org/pypi/{self.package}/json")
        json_response = response.json()

        return str(json_response["info"]["version"])

    @property
    def current_version_without_constraints(self) -> Version:
        version_without_constraints = re.sub(
            r"(?P<constraints>^[=<>~!]{0,3})", "", self.current_version
        )
        return parse(version_without_constraints)

    @property
    def version_constraints(self) -> str:
        parsed_constraints = re.search(
            r"(?P<constraints>^[=<>~!]{0,3})", self.current_version
        )
        return parsed_constraints.group()

    @property
    def latest_version_with_constraints(self) -> str:
        return f"{self.version_constraints}{self.latest_version}"

    @property
    def requires_update(self) -> bool:
        return self.current_version_without_constraints < parse(self.latest_version)


@dataclass
class Pipfile_Dependencies:
    packages: List[Dependency] = field(default_factory=list)
    dev_packages: List[Dependency] = field(default_factory=list)

    def load_toml_data(self, toml_file: TOMLFile):
        for package, version in toml_file.toml_data.get("packages").items():
            self.packages.append(Dependency(package=package, current_version=version))
        
        for package, version in toml_file.toml_data.get("dev-packages").items():
            self.dev_packages.append(Dependency(package=package, current_version=version))
         
    def all_dependencies(self):
        for dependency in self.packages + self.dev_packages:
            yield dependency
    
    def package_dependencies(self):
        for dependency in self.packages:
            if dependency.requires_update:
                yield dependency

    def dev_package_dependencies(self):
        for dependency in self.dev_packages:
            if dependency.requires_update:
                yield dependency
