"""Defines the Meme Quote Model"""
class QuoteModel():
    def __init__(self, body:str, author:str):
        """New quote model"""
        self.body = body
        self.author = author

    def __repr__(self):
        """return "body text" - author"""
        return f'\"{self.body}\" - {self.author}'
    
    def __str__(self):
        """Return 'str(self)'."""
        return self.body + " - " + self.author