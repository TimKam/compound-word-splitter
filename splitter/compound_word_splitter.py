# -*- coding: utf-8 -*-

import enchant, sys

# to be able to support Python 2 & 3
if sys.version_info[0] > 2:
    unicode = str


def __concat(object1, object2):
    if isinstance(object1, str) or isinstance(object1, unicode):
        object1 = [object1]
    if isinstance(object2, str) or isinstance(object2, unicode):
        object2 = [object2]
    return object1 + object2


def __capitalize_first_char(word):
    return word[0].upper() + word[1:]


def split(word, language='en_us'):
    dictionary = enchant.Dict(language)
    max_index = len(word)
    for index, char in enumerate(word):
        left_compound = word[0:max_index-index]
        right_compound_1 = word[max_index-index:max_index]
        right_compound_2 = word[max_index-index+1:max_index]
        if right_compound_1:
            right_compound1_upper = right_compound_1[0].isupper()
        if right_compound_2:
            right_compound2_upper = right_compound_2[0].isupper()
        if index > 0 and len(left_compound) > 1 and not dictionary.check(left_compound):
            left_compound = __capitalize_first_char(left_compound)
        is_left_compound_valid_word = len(left_compound) > 1 and dictionary.check(left_compound)
        if is_left_compound_valid_word and \
                ((not split(right_compound_1, language) == '' and not right_compound1_upper) \
                or right_compound_1 == ''):
            return [compound for compound in __concat(left_compound, split(right_compound_1, language))\
                    if not compound == '']
        elif is_left_compound_valid_word and word[max_index-index:max_index-index+1] == 's' and \
            ((not split(right_compound_2, language) == '' and not right_compound2_upper) \
            or right_compound_2 == ''):
            return [compound for compound in __concat(left_compound, split(right_compound_2, language))\
                    if not compound == '']
    if not word == '' and dictionary.check(word):
        return word
    elif not word == '' and dictionary.check(__capitalize_first_char(word)):
        return __capitalize_first_char(word)
    else:
        return ''
