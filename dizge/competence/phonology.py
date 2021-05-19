# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2021 Mehmet Umut Mutlu, Nazlıcan Yetimaslan, İlker Atagun
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import dizge.tools.phonology as tp


# PHONOLOGICAL STRUCTURES
class Phoneme:
    """

    """
    def __init__(self, phonemeID, grapheme):
        """

        :param phonemeID:
        :param grapheme:
        """
        self.phonemeID = phonemeID  # her bir sesbirime ait benzersiz kimlik
        self.grapheme = grapheme  # yazıbirim


class Consonant(Phoneme):
    """

    """
    def __init__(self, phonemeID, grapheme, manner, place, voicing):
        """

        :param phonemeID:
        :param grapheme:
        :param manner:
        :param place:
        :param voicing:
        """
        Phoneme.__init__(self, phonemeID, grapheme)
        self.manner = manner  # çıkış biçimi
        self.place = place  # çıkış yeri
        self.voicing = voicing  # ötümlülük

    def getManner(self):
        """

        :return:
        """
        if self.manner == 1:
            return "patlamalı"  # plosive
        elif self.manner == 2:
            return "genizsil"  # nasal
        elif self.manner == 3:
            return "titrek"  # trill
        elif self.manner == 4:
            return "dokunmalı veya çarpmalı"  # tap or flap
        elif self.manner == 5:
            return "sürtünmeli"  # fricative
        elif self.manner == 6:
            return "yan sürtünmeli"  # lateral fricative
        elif self.manner == 7:
            return "sürtünmesiz"  # approximant
        elif self.manner == 8:
            return "yan sürtünmesiz"  # lateral approximant
        else:
            return "hata"  # error

    def getPlace(self):
        """

        :return:
        """
        if self.place == 1:
            return "çift-dudaksıl"  # bilabial
        elif self.place == 2:
            return "dişsil-dudaksıl"  # labiodental
        elif self.place == 3:
            return "dişsil"  # dental
        elif self.place == 4:
            return "diş-yuvasıl"  # alveolar
        elif self.place == 5:
            return "artdiş-yuvasıl"  # postalveolar
        elif self.place == 6:
            return "üstdamaksıl"  # retroflex
        elif self.place == 7:
            return "damaksıl"  # palatal
        elif self.place == 8:
            return "artdamaksıl"  # velar
        elif self.place == 9:
            return "küçük-dilsil"  # uvular
        elif self.place == 10:
            return "yutaksıl"  # pharyngeal
        elif self.place == 11:
            return "gırtlaksıl"  # glottal
        else:
            return "hata"  # error

    def getVoicing(self):
        """

        :return:
        """
        if self.voicing == 0:
            return "ötümsüz"  # voiceless
        elif self.voicing == 1:
            return "ötümlü"  # voiced
        else:
            return "hata"  # error


class Vowel(Phoneme):
    """

    """
    def __init__(self, phonemeID, grapheme, rounding, mandible, tongue):
        """

        :param phonemeID:
        :param grapheme:
        :param rounding:
        :param mandible:
        :param tongue:
        """
        Phoneme.__init__(self, phonemeID, grapheme)
        self.rounding = rounding
        self.mandible = mandible
        self.tongue = tongue

    def getRounding(self):
        """

        :return:
        """
        if self.rounding == 0:
            return "düz"  # unrounded
        elif self.rounding == 1:
            return "yuvarlak"  # rounded
        else:
            return "hata"  # error

    def getMandible(self):
        """

        :return:
        """
        if self.mandible == 1:
            return "kapalı"  # close
        elif self.mandible == 2:
            return "yarı-kapalı"  # close-mid
        elif self.mandible == 3:
            return "yarı-açık"  # open-mid
        elif self.mandible == 4:
            return "açık"  # open
        else:
            return "hata"  # error

    def getTongue(self):
        """

        :return:
        """
        if self.tongue == 1:
            return "öndil"  # front
        elif self.tongue == 2:
            return "ortadil"  # central
        elif self.tongue == 3:
            return "arkadil"  # back
        else:
            return "hata"  # error

    # def getHeight(self):
    #     if self.height == 0:
    #         return "alçak" # low
    #     elif self.height == 1:
    #         return "yüksek" # high
    #     else:
    #         return "hata" # error


# PHONOLOGICAL UNITS
# VOWELS
v001 = Vowel("v001", "a", 0, 4, 3)
v002 = Vowel("v002", "e", 0, 4, 1)
v003 = Vowel("v003", "o", 1, 4, 3)
v004 = Vowel("v004", "ö", 1, 4, 1)
v005 = Vowel("v005", "i", 0, 1, 1)
v006 = Vowel("v006", "ı", 0, 1, 2)
v007 = Vowel("v007", "u", 1, 1, 3)
v008 = Vowel("v008", "ü", 1, 1, 1)
vowels = [v001, v002, v003, v004, v005, v006, v007, v008]

# CONSONANTS
c001 = Consonant("c001", "p", 1, 1, 0)
c002 = Consonant("c002", "b", 1, 1, 1)
c003 = Consonant("c003", "t", 1, 3, 0)
c004 = Consonant("c004", "d", 1, 3, 1)
c005 = Consonant("c005", "k", 1, 8, 0)
c006 = Consonant("c006", "g", 1, 8, 1)
c007 = Consonant("c007", "f", 5, 2, 0)
c008 = Consonant("c008", "v", 5, 2, 1)
c009 = Consonant("c009", "s", 5, 3, 0)
c010 = Consonant("c010", "z", 5, 3, 1)
c011 = Consonant("c011", "ş", 5, 5, 0)
c012 = Consonant("c012", "j", 5, 5, 1)
c013 = Consonant("c013", "ç", 1, 5, 0)
c014 = Consonant("c014", "c", 1, 5, 1)
c015 = Consonant("c015", "h", 5, 11, 0)
c016 = Consonant("c016", "y", 7, 7, 1)
c017 = Consonant("c017", "m", 2, 1, 1)
c018 = Consonant("c018", "n", 2, 3, 1)
c019 = Consonant("c019", "r", 4, 4, 1)
c020 = Consonant("c020", "l", 8, 5, 1)
consonants = [c001, c002, c003, c004, c005, c006, c007, c008, c009, c010,
              c011, c012, c013, c014, c015, c016, c017, c018, c019, c020]


# FEATURE FUNCTIONS
def isVowel(phoneme):
    """

    :param phoneme:
    :return:
    """
    if phoneme in [i.grapheme for i in vowels]:
        return True
    else:
        return False


def isUnrounded(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.rounding for i in vowels if i.grapheme == phoneme] == [0]:
        return True
    else:
        return False


def isRounded(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.rounding for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isClose(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.mandible for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isCloseMid(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.mandible for i in vowels if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False


def isOpenMid(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.mandible for i in vowels if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False


def isOpen(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.mandible for i in vowels if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False


def isFront(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.tongue for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isCentral(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.tongue for i in vowels if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False


def isBack(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.tongue for i in vowels if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False


def isConsonant(phoneme):
    """

    :param phoneme:
    :return:
    """
    if phoneme in [i.grapheme for i in consonants]:
        return True
    else:
        return False


def isPlosive(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isNasal(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False


def isTrill(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False


def isTaporFlap(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False


def isFricative(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [5]:
        return True
    else:
        return False


def isLateralFricative(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [6]:
        return True
    else:
        return False


def isApproximant(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [7]:
        return True
    else:
        return False


def isLateralApproximant(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [8]:
        return True
    else:
        return False


def isBilabial(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isLabiodental(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False


def isDental(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False


def isAlveolar(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False


def isPostalveolar(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [5]:
        return True
    else:
        return False


def isRetroflex(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [6]:
        return True
    else:
        return False


def isPalatal(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [7]:
        return True
    else:
        return False


def isVelar(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [8]:
        return True
    else:
        return False


def isUvular(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [9]:
        return True
    else:
        return False


def isPharyngeal(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [10]:
        return True
    else:
        return False


def isGlottal(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.place for i in consonants if i.grapheme == phoneme] == [11]:
        return True
    else:
        return False


def isVoiced(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.voicing for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False


def isVoiceless(phoneme):
    """

    :param phoneme:
    :return:
    """
    if [i.voicing for i in consonants if i.grapheme == phoneme] == [0]:
        return True
    else:
        return False


def isInitialWord(syllableCounter, phonemeCounter):
    """

    :param syllableCounter:
    :param phonemeCounter:
    :return:
    """
    if syllableCounter == 1 and phonemeCounter == 1:
        return True
    else:
        return False


def isFinalWord(syllableCounter, phonemeCounter, seq):
    """

    :param syllableCounter:
    :param phonemeCounter:
    :param seq:
    :return:
    """
    length = 0
    for syl in seq:
        length += len(syl)
    currentIndex = tp.findMyIndex(syllableCounter, phonemeCounter, seq)
    if length - 1 == currentIndex:
        return True
    else:
        return False


def getTongueSyllable(syllable):
    """

    :param syllable:
    :return:
    """
    for phoneme in syllable:
        if isVowel(phoneme):
            feature = [i.tongue for i in vowels if i.grapheme == phoneme][0]
    return feature
