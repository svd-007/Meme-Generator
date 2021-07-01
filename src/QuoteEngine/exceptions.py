"""A representation of Exception to handle inconsistent filetypes."""


class InvalidExtensionError(Exception):
    """
    Exception raised if filetype is not valid.

    Attributes:
    -----------
    `ext`: str
        filetype of the given file.

    `msg`: str
        error message in case exception is raised.
    """

    def __init__(self, ext: str) -> None:
        """Initialise the exception."""
        self.ext = ext
        self.msg = (f'Invalid file extension ".{self.ext}" provided.')
        super().__init__(self.msg)