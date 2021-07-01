"""Represent a class, providing an interface to parse various filetypes."""

from .model import QuoteModel
from .ingestor_interface import IngestorInterface
from .txt_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from typing import List


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
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a file.

        Parameters:
        -----------
        `path`: str
            path of the file to be parsed.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
