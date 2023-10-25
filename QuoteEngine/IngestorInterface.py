"""Create class and absract methods using ABC."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for the Ingestor classes of specific file types."""

    allowed_extension = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Validate whether a class can be ingested and parsed."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create ingest pathway and returns a quote to QuoteModel."""
        pass
