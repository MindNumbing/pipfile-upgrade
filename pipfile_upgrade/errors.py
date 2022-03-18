class NeedsHumanAttention(Exception):
    """The system doesn't know how to compare these"""

    def __init__(self, message: str):
        super().__init__(message)
