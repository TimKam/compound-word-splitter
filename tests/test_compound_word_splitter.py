# -*- coding: utf-8 -*-

from splitter import split


# it should split compound word (English)
def test_split_english():
    split_result = split('artutility', 'en_us')
    assert split_result[0] == 'art', '%s != "art"' % (split_result[0])
    assert split_result[1] == 'utility', '%s != "utility"' % (split_result[1])
    assert len(split_result) == 2, '%s != 2' % (len(split_result))


# should split German compound word
def test_split_german():
    split_result = split('Glossarelement', 'de_de')
    assert split_result[0] == 'Glossar', '%s != "Glossar"' % (split_result[0])
    assert split_result[1] == 'Element', '%s != "Element"' % (split_result[1])


# should split German compound word that contains a dictionary word with a suffixed `s`
def test_split_german_suffix_s():
    split_result = split('Effektivitätsberechnung', 'de_de')
    assert split_result[0] == 'Effektivität', '%s != "Effektivität"' % (split_result[0])
    assert split_result[1] == 'Berechnung', '%s != "Berechnung"' % (split_result[1])


# should split German compound word that contains a dictionary word that ends with `s`
def test_split_ends_with_s():
    split_result = split('Maushäuschen', 'de_de')
    assert split_result[0] == 'Maus', '%s != "Maus"' % (split_result[0])
    assert split_result[1]  == u'Häuschen'.encode('utf8'), '%s != "Häuschen"' % (split_result[1])


# should split German compound word that consists of three dictionary words
def test_split_german_three_compounds():
    split_result = split('Effektivitätsberechnungsformular', 'de_de')
    print split_result
    assert split_result[0] == 'Effektivität', '%s != "Effektivität"' % (split_result[0])
    assert split_result[1] == 'Berechnung', '%s != "Berechnung"' % (split_result[1])
    assert split_result[2] == 'Formular', '%s != "Formular"' % (split_result[2])

# should split compound word into largest possible dictionary words
def test_split_largest_possible_words():
    split_result = split('testresult', 'en_us')
    assert split_result[0] == 'test', '%s != "test"' % (split_result[0])
    assert split_result[1] == 'result', '%s != "result"' % (split_result[1])


# should return an empty string if the word is not split-able
def test_split_incorrectly_capitalized():
    split_result = split('Endereignissdfsdfsdf', 'de_de')
    assert split_result == '', '%s != ""' % split_result


# should return an empty string if the word is incorrectly capitalized
def test_split_incorrectly_capitalized():
    split_result = split('StartEreignis', 'de_de')
    assert split_result == '', '%s != ""' % split_result
