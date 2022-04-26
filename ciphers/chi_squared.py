from ciphers.constants import Constants


class ChiSquared:
    """Represents an object to compare the letter frequency of a potential
    decryption to English using a chi squared test
    """

    def calculate_chi_squared(self, decryption):
        """Runs a chi squared test to compare the letter frequency of a potential
        decryption to English

        (OV - EV) ^ 2 / EV

        Args:
            decryption (Decryption): A Decryption object containing plaintext

        Returns:
            int: the chi squared result
        """
        chi_totals = []
        for key in Constants.CHAR_F.keys():
            observed = decryption.text.count(key)
            expected = len(decryption.text) * (Constants.CHAR_F[key] / 100)
            chi_letter_total = ((observed - expected) ** 2) / expected
            chi_totals.append(chi_letter_total)

        return sum(chi_totals)
