"""Represent a sub-class of `IngestorInterface` to parse `.pdf` files."""

from .ingestor_interface import IngestorInterface
from .model import QuoteModel
from typing import List
import subprocess
from os import remove
from random import randint


class PDFIngestor(IngestorInterface):
    """Sub-class of `IngestorInterface` to parse `.pdf` files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a `.pdf` file.

        Parameters:
        -----------
        `path`: str
            path of the `.pdf` file to be parsed.
        """
        tmp = f"./_data/DogQuotes/{randint(0, 1000)}.txt"
        program = "./xpdf-tools-win-4.03/bin64/pdftotext.exe"
        subprocess.call([program, '-raw', path, tmp])

        with open(tmp, 'r') as infile:
            quotes = [QuoteModel(body=line.strip().split(' - ')[0],
                                 author=line.strip().split(' - ')[1])
                      for line in infile if len(line) > 1]
        remove(tmp)

        return quotes
