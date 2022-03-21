class InvalidDirectoryError(NotADirectoryError):
    """The provided path does not resolve to a vald directory"""

    def __init__(self, message: str):
        super().__init__(message)


class MissingPipfileError(FileNotFoundError):
    """The provided directory does not contain a pipfile"""

    def __init__(self, message: str):
        super().__init__(message)
