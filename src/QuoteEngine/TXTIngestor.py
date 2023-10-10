from typing import List

from QuoteEngine import IngestorInterface
from QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

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

