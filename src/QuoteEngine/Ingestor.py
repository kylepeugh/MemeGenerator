"""Main Library with pathways to specific file-type ingestors."""

from typing import List 
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
#from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Captures all of the ingestor classes and assigns the correct ingestor for the specific file type given."""

    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quote = []
        TXT_file = open(path, 'r')
        
        for line in TXT_file:
            if line is not None:
                parse = line.split('-')
                pullled_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                quote.append(pullled_quote)
        TXT_file.close()
        return quote
        