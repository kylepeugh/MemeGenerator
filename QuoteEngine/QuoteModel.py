"""Defines the Meme Quote Model."""


class QuoteModel():
    """Encapsulate the body and author of a new quote."""

    def __init__(self, body: str, author: str):
        """Create new quote model."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return "body text" - author."""
        return f'\"{self.body}\" - {self.author}'

    def __str__(self):
        """Return 'str(self)'."""
        return self.body + " - " + self.author
