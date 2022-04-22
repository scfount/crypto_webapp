

class Decryption:

    def __init__(self, text, key) -> None:
        self.text = text
        self.key = key
        self.chi_squared = None

    def __str__(self) -> str:
        return f"text: {self.text} key: {self.key} Chi: {self.chi_squared}"

    def __lt__(self, other):
        return self.chi_squared < other.chi_squared
