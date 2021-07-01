"""A Representation of a `Quote` encapsulating its body and author."""


class QuoteModel:
    """
    A class to encapsulate the `body` and the `author` of a quote.

    Attributes
    ----------
    `body`: str
        the body of the quote.

    `author`: str
        the author of the quote.
    """

    def __init__(self, body: str, author: str):
        """
        Create a new `QuoteModel`.

        Parameters
        ----------
        `body`: str
            the body of the quote.

        `author`: str
            the author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """
        Return `str(self)`.

        A string representation of this object.
        """
        return f"{self.body} - {self.author}"

    def __repr__(self) -> str:
        """
        Return `repr(self)`.

        A computer readable string representation of this object.
        """
        return f"QuoteModel(body={self.body}, author={self.author})"
