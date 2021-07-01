"""Represent a sub-class of `IngestorInterface` to parse `.docx` files."""

from .ingestor_interface import IngestorInterface
from .model import QuoteModel
from docx import Document
from typing import List


class DocxIngestor(IngestorInterface):
    """Sub-class of `IngestorInterface` to parse `.docx` files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Return a list of `QuoteModel` objects after parsing a `.docx` file.

        Parameters:
        -----------
        `path`: str
            path of the `.docx` file to be parsed.
        """
        doc = Document(path)
        return [QuoteModel(body=para.text.split(' - ')[0],
                           author=para.text.split(' - ')[1])
                for para in doc.paragraphs if len(para.text) > 1]
