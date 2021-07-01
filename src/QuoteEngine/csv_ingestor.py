"""Represent a sub-class of `IngestorInterface` to parse `.csv` files."""

from .ingestor_interface import IngestorInterface
from .model import QuoteModel
from pandas import read_csv
from typing import List


class CSVIngestor(IngestorInterface):
    """Sub-class of `IngestorInterface` to parse `.csv` files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a `.csv` file.

        Parameters:
        -----------
        `path`: str
            path of the `.csv` file to be parsed.
        """
        df = read_csv(path)
        return [QuoteModel(body=row.body,
                           author=row.author)
                for row in df.itertuples()]
