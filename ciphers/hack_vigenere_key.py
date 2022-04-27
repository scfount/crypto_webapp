import collections
from itertools import combinations
import itertools
import re
from ciphers.constants import Constants
from ciphers.shift import Shift


class HackVigenereKey:
    """Represents an object to break the Vigenere cipher
    """

    def hack_key(self, ciphertext):
        """Generates a list of possible Vigenere key lengths based on the 
        provided ciphertext using the kasiski analysis:
        - get repeated substrings of length 3
        - find distance between any repeated, length-3 substrings
        - count all factors of found distances, using higher occurring factors
        as likely key lengths
        - I modified to only look at factors >= 4 on first pass as 2 and 3
        tend to dominate the count

        Args:
            ciphertext (String): The ciphertext used to generate teh possible
            key lengths

        Returns:
            list: A list of ints representing possible key lengths to decrypt
            the ciphertext
        """
        # Run Kasiski examination to find key length
        # find all repeated substrings of length 3, decrease if needed
        for sub_len in range(3, 0, -1):
            kasiski_list = self.get_all_substrings(ciphertext, sub_len)
            # add all to dict to count frequency of each substring
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

    def get_all_substrings(self, ciphertext, length):
        """Generates a list of all the substrings in the ciphertext of the 
        specified length

        Args:
            ciphertext (String): The string to generate substrings from
            length (int): The size of the desired substrings

        Returns:
            list: A list of all the specified length substrings
        """
        kasiski_list = [ciphertext[x:y] for x, y in combinations(
            range(len(ciphertext) + 1), r=2) if len(ciphertext[x:y]) == length]
        return kasiski_list

    def count_freq_substrings(self, kasiski_list):
        """Count the number of occurrences for each substring in provided list

        Args:
            kasiski_list (list): A list of n-length substrings

        Returns:
            dictionary: A dictionary where the key is a substring and the value
            is its occurrence frequency
        """
        kasiski_dict = {}
        for substring in kasiski_list:
            if substring in kasiski_dict:
                kasiski_dict[substring] += 1
            else:
                kasiski_dict[substring] = 1
        return kasiski_dict

    def get_repeat_substrings(self, kasiski_dict):
        """Finds all the substrings that occur more than one time in the ciphertext

        Args:
            kasiski_dict (dictionary): A dictionary where the key is a substring and the value
            is its occurrence frequency

        Returns:
            list: A list of only the substrings that occur more than once
        """
        kasiski_repeated = []
        for substr, freq in kasiski_dict.items():
            if freq > 1:
                kasiski_repeated.append(substr)
        return kasiski_repeated

    def calc_distance_between_substrings(self, ciphertext, kasiski_repeated):
        """Finds the distance between repeated substrings, for all occurrences. 

        Finds the start index for each repeated substing, then finds the difference 
        between repeated substring start indexes, for all substrings. 

        Args:
            ciphertext (String): The encrypted text
            kasiski_repeated (list): A list of all the repeated substrings

        Returns:
            list: A list representing all the distances between each repeated 
            substring
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

    def estimate_key_length(self, distance_list):
        """Finds an estimated key length by gererating a list of factors from
        the list of distances between repeated substrings. Looks for the 
        highest occuring factors. Ignores factors 1, 2, and 3 due to tendency
        to always occur frequently.

        Args:
            distance_list (list): a list of ints, each representing the
            distance between a repeated substing

        Returns:
            list: A list of the most likely key lengths
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
        """Finds the top two most likely key lengths >= 4 based on how
        frequently the factors occur

        Args:
            factor_count (list): A list of all the factors generated from 
            the distance list

        Returns:
            list: A list of the top two most likely key lengths >= 4
        """
        key_length_list = []
        most_common = collections.Counter(factor_count).most_common(2)

        for pair in most_common:
            key_length_list.append(pair[0])

        return key_length_list

    def guess_keys(self, ciphertext, length_attempt):
        """Generates a list of possible Vigenere keys based on key length

        Args:
            ciphertext (String): The encrypted text
            length_attempt (int): The length of the key for this attempt

        Returns:
            list: A list of Strings containing most likely keys of this length
        """
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
        """Generates a subgroup of the ciphertext by taking every n'th letter,
        starting at a specified index between 0 and n, where n is the key length

        Args:
            ciphertext (String): The encrypted text
            start (int): The index to start at within the ciphertext
            skip (int): The key length, aka the amount of indices to skip

        Returns:
            String: A subgroup of the ciphertext
        """
        subgroup_list = []
        while start < len(ciphertext):
            subgroup_list.append(ciphertext[start])
            start += skip
        subgroup = "".join(subgroup_list)
        return subgroup

    def get_best_shifts(self, decryptions):
        """Iterate through list of shift_decrypt_no_key Decryptions, grabbing
        the shift values that generate a low chi squared value based on their
        frequency analysis. Low = below the threshold of 25

        If none meet that criteria, return best two shift values

        Args:
            decryptions (list): A list of shift_decrypt_no_key Decryptions for
            this position in the key

        Returns:
            list: A list of ints representing best shift values for this position
            in the key
        """
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
        """Translates the retrieved shift values from a number to their
        respective letter in the alphabet:
        a = 0
        ...
        z = 25

        Args:
            shifts (list): A list of ints representing shift values for this
            position in the key

        Returns:
            list: A list of Chars representing the letter value for this
            position in the key
        """
        best_letters = []
        for shift in shifts:
            best_letters.append(Constants.ALPHABET_NUMBERS[shift])
        return best_letters
