"""
QuoteEngine module.

This module is responsible for ingesting many types of files that contain
quotes. It comprises of multiple classes having complex inheritance and is
composed of classmethods facilitating a design to extract quotes line-by-line
from files of several filetypes.

A final `Ingestor` class realizes the `IngestorInterface` abstract base class
and encapsulates the helper classes. It implements logic to select the
appropriate helper for a given file based on filetype.
"""

from .model import QuoteModel
from .ingestor_interface import IngestorInterface
from .txt_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .ingestor import Ingestor
