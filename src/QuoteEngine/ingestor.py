"""Represent a class, providing an interface to parse various filetypes."""

import os
from typing import List

from .model import QuoteModel
from .ingestor_interface import IngestorInterface
from .txt_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor

from .exceptions import InvalidExtensionError


class Ingestor(IngestorInterface):
    """
    Sub-class of `IngestorInterface`, giving a single interface to load a file.

    This class encapsulates all the ingestors to provide a single interface to
    load any supported filetype.

    This class realises from and acts as an interface for `TextIngestor`,
    `CSVIngestor`, `DocxIngestor` and `PDFIngestor` to parse files belonging to
    respective filetypes.
    """

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def validate_extension(cls, ext: str) -> None:
        """
        Assert whether given extension belongs to the list of valid extensions.

        Raise `InvalidExtensionError` if not a valid extension.
        """
        if ext not in [ingestor.allowed_extensions[0] for
                       ingestor in cls.ingestors]:
            raise InvalidExtensionError(ext)

    @staticmethod
    def validate_filename(filename: str) -> None:
        """
        Assert whether given filename is present in the `DogQuotes` directory.

        Raise `FileNotFoundError` if not found.
        """
        if filename not in os.listdir("./_data/DogQuotes/"):
            raise FileNotFoundError(f'FileNotFoundError: "{filename}"'
                                    ' not found in directory.')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a file.

        Parameters:
        -----------
        `path`: str
            path of the file to be parsed.
        """
        ext = path.split(".")[-1]
        filename = path.split("/")[-1]
        # First try-except block to catch any exceptions w.r.t
        # invalid extension or invalid filename.
        try:
            cls.validate_extension(ext)
            cls.validate_filename(filename)
        except InvalidExtensionError as inv_ext_err:
            print(inv_ext_err)
        except FileNotFoundError as fnf_err:
            print(fnf_err)
        else:
            # Second try-except block to catch any exceptions
            # while parsing the file.
            try:
                for ingestor in cls.ingestors:
                    if ingestor.can_ingest(path):
                        return ingestor.parse(path)
            except Exception:
                print(f"ParsingError: Error occured while parsing {filename}.")
