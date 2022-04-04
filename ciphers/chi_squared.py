
from ciphers.constants import Constants


class Chi_Squared:

    def __init__(self, text_length) -> None:
        self.text_length = text_length

    def calculate_chi_squared(self, decryption):
        # (OV - EV) ^ 2 / EV
        chi_totals = []
        for key in Constants.CHAR_F.keys():
            observed = decryption.text.count(key)
            expected = self.text_length * (Constants.CHAR_F[key] / 100)
            chi_letter_total = ((observed - expected) ** 2) / expected
            chi_totals.append(chi_letter_total)
        return sum(chi_totals)
