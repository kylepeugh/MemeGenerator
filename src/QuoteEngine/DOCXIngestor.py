from typing import List
import docx
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """ Docx file ingestor. Returns a list of quotes. """

    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        #if not cls.can_ingest(path):
           #raise Exception('cannot ingest exception')

        quote = []
        docu = docx.Document(path)

        for para in docu.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].strip(' "'),
                                       parse[1])
                quote.append(new_quote)

        return quote