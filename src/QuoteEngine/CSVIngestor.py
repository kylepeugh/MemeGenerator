"""File used to parse CSV files using a strategy object class."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Object class for parsing CSV files
    
    param allowed-extensions: File pathway allowed in this ingestor."""
    allowed_extension = ['CSV']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quote = []

        dataframe = pandas.read_csv(path, header =0)

        for row in dataframe.iterrows:
            pulled_quote = QuoteModel(body=row['body'],
                                      author=row['author'])
            quote.append(pulled_quote)
            
        return quote


        
        


