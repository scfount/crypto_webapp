

class Decryption:
    """Represents a Decryption object
    """

    def __init__(self, text, key) -> None:
        """Initializes a new Decryption

        Args:
            text (String): The decrypted text
            key (String || int): The key used to decrypt
        """
        self.text = text
        self.key = key
        self.chi_squared = None
        self.isReliable = None
        self.details = None
        self.decryption_score = None
        self.language = None

    def __str__(self) -> str:
        return f"text: {self.text} key: {self.key} Chi: {self.chi_squared}"

    def __lt__(self, other):
        return self.chi_squared < other.chi_squared
