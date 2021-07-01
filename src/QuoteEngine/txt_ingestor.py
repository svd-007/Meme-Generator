"""Represent a sub-class of `IngestorInterface` to parse `.txt` files."""

from .ingestor_interface import IngestorInterface
from .model import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """Sub-class of `IngestorInterface` to parse `.txt` files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a `.txt` file.

        Parameters:
        -----------
        `path`: str
            path of the `.txt` file to be parsed.
        """
        with open(path, 'r') as infile:
            return [QuoteModel(body=line.split(' - ')[0],
                               author=line.split(' - ')[1])
                    for line in infile if len(line) > 1]
