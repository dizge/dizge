# -*- coding: utf-8 -*-
import dizge

# SIMULATION OF PHONETIC COMPETENCE
for i in [vars(phoneme) for phoneme in dizge.vowels]:
    print(i)
# {'phonemeID': 'v001', 'grapheme': 'a', 'rounding': 0, 'mandible': 4, 'tongue': 3}
# {'phonemeID': 'v002', 'grapheme': 'e', 'rounding': 0, 'mandible': 4, 'tongue': 1}
# {'phonemeID': 'v003', 'grapheme': 'o', 'rounding': 1, 'mandible': 4, 'tongue': 3}
# {'phonemeID': 'v004', 'grapheme': 'ö', 'rounding': 1, 'mandible': 4, 'tongue': 1}
# {'phonemeID': 'v005', 'grapheme': 'i', 'rounding': 0, 'mandible': 1, 'tongue': 1}
# {'phonemeID': 'v006', 'grapheme': 'ı', 'rounding': 0, 'mandible': 1, 'tongue': 2}
# {'phonemeID': 'v006', 'grapheme': 'ı', 'rounding': 0, 'mandible': 1, 'tongue': 2}
# {'phonemeID': 'v007', 'grapheme': 'u', 'rounding': 1, 'mandible': 1, 'tongue': 3}
# {'phonemeID': 'v008', 'grapheme': 'ü', 'rounding': 1, 'mandible': 1, 'tongue': 1}

for j in [vars(phoneme) for phoneme in dizge.consonants]:
    print(j)
# {'phonemeID': 'c001', 'grapheme': 'p', 'manner': 1, 'place': 1, 'voicing': 0}
# {'phonemeID': 'c002', 'grapheme': 'b', 'manner': 1, 'place': 1, 'voicing': 1}
# {'phonemeID': 'c003', 'grapheme': 't', 'manner': 1, 'place': 3, 'voicing': 0}
# {'phonemeID': 'c004', 'grapheme': 'd', 'manner': 1, 'place': 3, 'voicing': 1}
# {'phonemeID': 'c005', 'grapheme': 'k', 'manner': 1, 'place': 8, 'voicing': 0}
# {'phonemeID': 'c006', 'grapheme': 'g', 'manner': 1, 'place': 8, 'voicing': 1}
# {'phonemeID': 'c007', 'grapheme': 'f', 'manner': 5, 'place': 2, 'voicing': 0}
# {'phonemeID': 'c008', 'grapheme': 'v', 'manner': 5, 'place': 2, 'voicing': 1}
# {'phonemeID': 'c009', 'grapheme': 's', 'manner': 5, 'place': 3, 'voicing': 0}
# {'phonemeID': 'c010', 'grapheme': 'z', 'manner': 5, 'place': 3, 'voicing': 1}
# {'phonemeID': 'c011', 'grapheme': 'ş', 'manner': 5, 'place': 5, 'voicing': 0}
# {'phonemeID': 'c012', 'grapheme': 'j', 'manner': 5, 'place': 5, 'voicing': 1}
# {'phonemeID': 'c013', 'grapheme': 'ç', 'manner': 1, 'place': 5, 'voicing': 0}
# {'phonemeID': 'c014', 'grapheme': 'c', 'manner': 1, 'place': 5, 'voicing': 1}
# {'phonemeID': 'c015', 'grapheme': 'h', 'manner': 5, 'place': 11, 'voicing': 0}
# {'phonemeID': 'c016', 'grapheme': 'y', 'manner': 7, 'place': 7, 'voicing': 1}
# {'phonemeID': 'c017', 'grapheme': 'm', 'manner': 2, 'place': 1, 'voicing': 1}
# {'phonemeID': 'c018', 'grapheme': 'n', 'manner': 2, 'place': 3, 'voicing': 1}
# {'phonemeID': 'c019', 'grapheme': 'r', 'manner': 4, 'place': 4, 'voicing': 1}
# {'phonemeID': 'c020', 'grapheme': 'l', 'manner': 8, 'place': 5, 'voicing': 1}

# Feature Functions
print(dizge.isVowel("a"))  # True
print(dizge.isBilabial("g"))  # False

# TOOLS
# Separation into Syllables
print(dizge.syllable_p("ANKARA'DA     "))  # ['an', 'ka', 'ra', 'da']
print(dizge.syllable_p("Afyonkarahisarlılaştıramadıklarımızdanmışçasına"))
# ['af', 'yon', 'ka', 'ra', 'hi', 'sar', 'lı', 'laş', 'tı', 'ra', 'ma', 'dık', 'la', 'rı', 'mız', 'dan', 'mış', 'ça','sı', 'na']

# soft g Transformation Tool
print(dizge.softG("dağ"))  # 'da:'
print(dizge.softG("doğru"))  # 'doˑru'

# Phonetic Transcriptions Tool
print(dizge.g2p("ben"))  # 'bɛn'
print(dizge.g2p("kelebek"))  # 'cʰelɛbɛc'

# Simple Usage
words = ["ankara", "dil", "bilim", "dilbilim"]
result = dizge.analyze(words, ["g2p", "syllable_o", "syllable_p", "countSylable", "harmony"])
print(result)
