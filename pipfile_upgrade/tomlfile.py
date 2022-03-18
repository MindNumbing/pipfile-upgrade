from pathlib import Path

import tomlkit


class TOMLFile:
    def __init__(self, filepath: Path):
        self.filepath: Path = filepath
        self.toml_data: tomlkit.TOMLDocument = self.load_file()

    def load_file(self) -> tomlkit.TOMLDocument:
        with open(self.filepath, "r") as open_file:
            toml_data: tomlkit.TOMLDocument = tomlkit.load(open_file)
        return toml_data

    def save_file(self) -> None:
        with open(self.filepath, "w") as open_file:
            tomlkit.dump(self.toml_data, open_file)
