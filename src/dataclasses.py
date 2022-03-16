import re
from dataclasses import dataclass
from typing import Optional

from .errors import NeedsHumanAttention


@dataclass
class Semver:
    def __init__(self, version: str):
        match: Optional[re.Match[str]] = self.semver_re().search(version)
        if match is None:
            raise NeedsHumanAttention(
                f"The semver {version} does not meet regex requirements and should be updated manually"
            )

        self.constraints = match.groupdict().get("constraints")
        self.major = match.groupdict().get("major")
        self.minor = match.groupdict().get("minor")
        self.patch = match.groupdict().get("patch")
        self.prerelease = match.groupdict().get("prerelease")
        self.buildmetadata = match.groupdict().get("buildmetadata")

    @property
    def meta(self) -> str:
        return f"{self.prerelease or ''}{self.buildmetadata or ''}"

    @property
    def version(self) -> str:
        return f"{self.constraints or ''}{self.major}{'.' + self.minor if self.minor else ''}{'.' + self.patch if self.patch else ''}{self.meta or ''}"

    def __repr__(self) -> str:
        return self.version

    @staticmethod
    def semver_re() -> re.Pattern[str]:
        """
        Source: https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string

        With additional modification to include pipfile constraints capture group as well as to make minor / patch optional
        """
        constraints_capture = r"(?P<constraints>[=<>~]{0,2})"
        major_capture = r"(?P<major>0|[1-9]\d*)"
        minor_capture = r"(?P<minor>0|[1-9]\d*)?"
        patch_capture = r"(?P<patch>0|[1-9]\d*)?"
        pre_release_capture = r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
        build_metadata_capture = (
            r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
        )

        return re.compile(
            rf"^{constraints_capture}{major_capture}\.?{minor_capture}\.?{patch_capture}{pre_release_capture}{build_metadata_capture}$"
        )

    def newer_than(self, other: "Semver") -> bool:
        if self.major and other.major:
            if self.major > other.major:
                return True
            elif self.major < other.major:
                return False

        if self.minor and other.minor:
            if self.minor > other.minor:
                return True
            elif self.minor < other.minor:
                return False
        elif self.minor and not other.minor:
            return False
        elif not self.minor and other.minor:
            if other.minor == "0":
                return False
            return True

        if self.patch and other.patch:
            if self.patch > other.patch:
                return True
            elif self.patch < other.patch:
                return False
        elif self.patch and not other.patch:
            return False
        elif not self.patch and other.patch:
            if other.patch == "0":
                return False
            return True

        if self.meta and not other.meta:
            return False
        elif not self.meta and other.meta:
            return True
        elif not self.meta and not other.meta:
            return False
        elif self.meta and other.meta:
            if self.meta != other.meta:
                raise NeedsHumanAttention(
                    message="You should probably take a look at this"
                )
            else:
                return False
        return False


@dataclass
class Dependency:
    dependency_type: str
    package: str
    current_version: Semver
    latest_version: Semver

    def __repr__(self) -> str:
        return f"Package: {self.package}. Current version: {self.current_version}. Latest_version: {self.latest_version_with_constraints}"

    @property
    def latest_version_with_constraints(self) -> str:
        return f"{self.current_version.constraints}{self.latest_version.version}"

    @property
    def requires_update(self) -> bool:
        return self.latest_version.newer_than(self.current_version)
