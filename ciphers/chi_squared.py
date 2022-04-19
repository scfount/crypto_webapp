from ciphers.constants import Constants


class ChiSquared:

    def calculate_chi_squared(self, decryption):
        # (OV - EV) ^ 2 / EV
        chi_totals = []
        for key in Constants.CHAR_F.keys():
            observed = decryption.text.count(key)
            expected = len(decryption.text) * (Constants.CHAR_F[key] / 100)
            chi_letter_total = ((observed - expected) ** 2) / expected
            chi_totals.append(chi_letter_total)
        return sum(chi_totals)
