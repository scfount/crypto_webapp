import collections
from itertools import combinations
import itertools
import re
from ciphers.constants import Constants
from ciphers.shift import Shift


class HackVigenereKey:

    def hack_key(self, ciphertext):
        """_summary_

        Args:
            ciphertext (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Run Kasiski examination to find key length
        # find all repeated substrings of length 3
        for sub_len in range(3, 0, -1):
            kasiski_list = self.get_all_substrings(ciphertext, sub_len)
            # add all to dict to count frequency
            kasiski_dict = self.count_freq_substrings(kasiski_list)
            # iterate through dict and pull out substrings with a freq. greater than 1
            kasiski_repeated = self.get_repeat_substrings(kasiski_dict)
            if kasiski_repeated:
                break

        # get number of letters between repeats
        distance_list = self.calc_distance_between_substrings(
            ciphertext, kasiski_repeated)

        # count all factors for distances (excluding 1) to guess most likely key lengths
        possible_key_lengths = self.estimate_key_length(distance_list)

        return possible_key_lengths

    def estimate_key_length(self, distance_list):
        """_summary_

        Args:
            distance_list (_type_): _description_

        Returns:
            _type_: _description_
        """
        factor_list = []

        for distance in distance_list:
            for i in range(4, distance):
                if distance % i == 0:
                    factor_list.append(i)

        factor_count = collections.Counter(factor_list)

        key_length_list = self.isolate_top_key_lengths(factor_count)

        return key_length_list

    def isolate_top_key_lengths(self, factor_count):
        """_summary_

        Args:
            factor_count (_type_): _description_

        Returns:
            _type_: _description_
        """
        #  take values with top two counts
        key_length_list = []
        most_common = collections.Counter(factor_count).most_common(2)

        for pair in most_common:
            key_length_list.append(pair[0])

        return key_length_list

    def calc_distance_between_substrings(self, ciphertext, kasiski_repeated):
        """_summary_

        Args:
            ciphertext (_type_): _description_
            kasiski_repeated (_type_): _description_

        Returns:
            _type_: _description_
        """
        k_dict = {}
        for substring in kasiski_repeated:
            k_dict[substring] = [match.start()
                                 for match in re.finditer(substring, ciphertext)]
        distance_list = []
        for distances in k_dict.values():
            i = 0
            while i < len(distances)-1:
                distance_list.append(distances[i+1] - distances[i])
                i += 1
        return distance_list

    def get_all_substrings(self, ciphertext, length):
        """_summary_

        Args:
            ciphertext (_type_): _description_
            length (_type_): _description_

        Returns:
            _type_: _description_
        """
        kasiski_list = [ciphertext[x:y] for x, y in combinations(
            range(len(ciphertext) + 1), r=2) if len(ciphertext[x:y]) == length]
        return kasiski_list

    def count_freq_substrings(self, kasiski_list):
        """_summary_

        Args:
            kasiski_list (_type_): _description_

        Returns:
            _type_: _description_
        """
        kasiski_dict = {}
        for substring in kasiski_list:
            if substring in kasiski_dict:
                kasiski_dict[substring] += 1
            else:
                kasiski_dict[substring] = 1
        return kasiski_dict

    def get_repeat_substrings(self, kasiski_dict):
        """_summary_

        Args:
            kasiski_dict (_type_): _description_

        Returns:
            _type_: _description_
        """
        kasiski_repeated = []
        for substr, freq in kasiski_dict.items():
            if freq > 1:
                kasiski_repeated.append(substr)
        return kasiski_repeated

    def guess_keys(self, ciphertext, length_attempt):
        """_summary_

        Args:
            ciphertext (_type_): _description_
            length_attempt (_type_): _description_

        Returns:
            _type_: _description_
        """
        # key list = list of all possible string keys at this length
        key_list = []
        for i in range(length_attempt):
            subgroup = self.get_sub_group(ciphertext, i, length_attempt)
            shift = Shift(subgroup, "")
            decryptions = shift.decrypt_no_key()

            #  list of numbers indicating best shifts to try for this position
            best_shifts = self.get_best_shifts(decryptions)

            # transform list of shifts to list of letters
            best_letters = self.get_best_letters(best_shifts)

            key_list.append(best_letters)

        possible_keys = list(itertools.product(*key_list))

        return possible_keys

    def get_sub_group(self, ciphertext, start, skip):
        """_summary_

        Args:
            ciphertext (_type_): _description_
            start (_type_): _description_
            skip (_type_): _description_

        Returns:
            _type_: _description_
        """
        subgroup_list = []
        while start < len(ciphertext):
            subgroup_list.append(ciphertext[start])
            start += skip
        subgroup = "".join(subgroup_list)
        return subgroup

    def get_best_shifts(self, decryptions):
        # iterate through list of deccryptions
        # take n best chi-squared keys
        THRESHOLD = 25
        best_shifts = []
        for decryption in decryptions:
            if decryption.chi_squared < THRESHOLD:
                best_shifts.append(decryption.key)
        if not best_shifts:
            for i in range(2):
                best_shifts.append(decryptions[i].key)
        return best_shifts

    def get_best_letters(self, shifts):
        best_letters = []
        for shift in shifts:
            best_letters.append(Constants.ALPHABET_NUMBERS[shift])
        return best_letters
