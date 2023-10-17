"""File used to parse TXT files using a strategy object class."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """Object class for parsing TXT files.
    
    param allowed-extension: File pathway allowed in this ingestor."""
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')
        
        quote = []
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    pullled_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quote.append(pullled_quote)

            file.close()
            return quote

        """quote = []
        TXT_file = open(path, 'r')
        
        for line in TXT_file:
            if line is not None:
                parse = line.split('-')
                pullled_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                quote.append(pullled_quote)
        TXT_file.close()
        return quote"""