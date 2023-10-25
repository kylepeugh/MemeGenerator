"""File used to parse CSV files using a strategy object class."""
from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Object class for parsing CSV files.

    param allowed-extensions: File pathway allowed in this ingestor.
    """

    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse body and author from the .CSV file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest')
        quote = []
        dataframe = pandas.read_csv(path, header=0)

        for index, row in dataframe.iterrows():
            pulled_quote = QuoteModel(body=row['body'],
                                      author=row['author'])
            quote.append(pulled_quote)

        return quote
