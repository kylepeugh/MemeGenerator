"""File used to parse PDF files using a strategy object class."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """PDF class object for parsing a PDF file
    
    param allowed_extension: File Pathway allowed in this ingestor."""
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        
        tmp = f'./tmp_{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotxt', path, tmp])

        PDF_file = open(tmp, "r")
        quote = []

        for line in PDF_file.readlines:
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                pulled_quote = QuoteModel(parse[0].strip(' "'),
                                          parse[1].strip())
                quote.append(pulled_quote)
    
        PDF_file.close()
        os.remove(tmp)
        return quote





