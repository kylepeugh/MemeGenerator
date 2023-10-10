
from typing import List 
from QuoteEngine import IngestorInterface, QuoteModel
from DOCXIngestor import DOCXIngestor
from CSVIngestor import CSVIngestor
from TXTIngestor import TXTIngestor
from PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Captures all of the ingestor classes and assigns the correct ingestor for the specific file type given."""

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                    return ingestor.parse(path)

        