"""Represent an Abstract Base Class for Ingestor Interface."""

from abc import ABC, abstractmethod
from .model import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """
    Abstract Base Class for Ingestor Interface.

    This class defines:

    - A classmethod `can_ingest` to verify if a file is compatible with the
    ingestor class.

    - An abstractmethod `parse` for parsing the file content into a list of
    `QuoteModel` objects.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Return `True` if a file can be parsed by the ingestor.

        Parameters:
        -----------
        `path`: str
            path of the file to be parsed.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a file.

        Parameters:
        -----------
        `path`: str
            path of the file to be parsed.
        """
        pass
