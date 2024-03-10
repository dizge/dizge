# -*- coding: utf-8 -*-

import dizge.tools as tools

# PHONOLOGICAL STRUCTURES
class Phoneme:
    """Representing the phonemes in the linguistic competence of an ideal native speaker

    Args:
        phonemeID (str): An unique ID for each phoneme
        grapheme (str): The grapheme for each phoneme
    """

    def __init__(self, phonemeID: str, grapheme: str):
        """Representing the phonemes in the linguistic competence of an ideal native speaker

        Args:
            phonemeID (str): An unique ID for each phoneme
            grapheme (str): The grapheme for each phoneme
        """
        self.phonemeID = phonemeID
        self.grapheme = grapheme

class Consonant(Phoneme):
    """Representing the consonants in the linguistic competence of an ideal native speaker

    Args:
        phonemeID (str): An unique ID for each phoneme
        grapheme (str): The grapheme for each phoneme
        manner (int): The manner value of the phoneme according to IPA
        place (int): The place value of the phoneme according to IPA
        voicing (int): The voicing value of the phoneme according to IPA
    """

    def __init__(self, phonemeID: str, grapheme: str, manner: int, place: int, voicing: int):
        """Representing the consonants in the linguistic competence of an ideal native speaker

        Args:
            phonemeID (str): An unique ID for each phoneme
            grapheme (str): The grapheme for each phoneme
            manner (int): The manner value of the phoneme according to IPA
            place (int): The place value of the phoneme according to IPA
            voicing (int): The voicing value of the phoneme according to IPA
        """
        Phoneme.__init__(self, phonemeID, grapheme)
        self.manner = manner
        self.place = place
        self.voicing = voicing

    def getManner(self):
        """It returns the manner info."""

        if self.manner == 1:
            return "plosive"
        elif self.manner == 2:
            return "nasal"
        elif self.manner == 3:
            return "trill"
        elif self.manner == 4:
            return "tap or flap"
        elif self.manner == 5:
            return "fricative"
        elif self.manner == 6:
            return "lateral fricative"
        elif self.manner == 7:
            return "approximant"
        elif self.manner == 8:
            return "lateral approximant"
        else:
            return "error"

    def getPlace(self):
        """It returns the place info."""

        if self.place == 1:
            return "bilabial"
        elif self.place == 2:
            return "labiodental"
        elif self.place == 3:
            return "dental"
        elif self.place == 4:
            return "alveolar"
        elif self.place == 5:
            return "postalveolar"
        elif self.place == 6:
            return "retroflex"
        elif self.place == 7:
            return "palatal"
        elif self.place == 8:
            return "velar"
        elif self.place == 9:
            return "uvular"
        elif self.place == 10:
            return "pharyngeal"
        elif self.place == 11:
            return "glottal"
        else:
            return "error"

    def getVoicing(self):
        """It returns the voicing info."""

        if self.voicing == 0:
            return "voiceless"
        elif self.voicing == 1:
            return "voiced"
        else:
            return "error"

class Vowel(Phoneme):
    """Representing the vowels in the linguistic competence of an ideal native speaker

    Args:
        phonemeID (str): An unique ID for each phoneme
        grapheme (str): The grapheme for each phoneme
        rounding (int): The rounding value of the phoneme according to IPA
        mandible (int): The mandible value of the phoneme according to IPA
        tongue (int): The tongue value of the phoneme according to IPA
    """

    def __init__(self, phonemeID: str, grapheme: str, rounding: int, mandible: int, tongue: int):
        """Representing the vowels in the linguistic competence of an ideal native speaker

        Args:
            phonemeID (str): An unique ID for each phoneme
            grapheme (str): The grapheme for each phoneme
            rounding (int): The rounding value of the phoneme according to IPA
            mandible (int): The mandible value of the phoneme according to IPA
            tongue (int): The tongue value of the phoneme according to IPA
        """
         
        Phoneme.__init__(self, phonemeID, grapheme)
        self.rounding = rounding
        self.mandible = mandible
        self.tongue = tongue

    def getRounding(self):
        """It returns the rounding info."""

        if self.rounding == 0:
            return "unrounded"
        elif self.rounding == 1:
            return "rounded"
        else:
            return "error"

    def getMandible(self):
        """It returns the mandible info."""

        if self.mandible == 1:
            return "close"
        elif self.mandible == 2:
            return "close-mid"
        elif self.mandible == 3:
            return "open-mid"
        elif self.mandible == 4:
            return "open"
        else:
            return "error"

    def getTongue(self):
        """It returns the tongue info."""

        if self.tongue == 1:
            return "front"
        elif self.tongue == 2:
            return "central"
        elif self.tongue == 3:
            return "back"
        else:
            return "error"

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

# FEATURE CHECK FUNCTIONS
def isVowel(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """
    if phoneme in [i.grapheme for i in vowels]:
        return True
    else:
        return False

def isUnrounded(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is unrounded.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """
    if [i.rounding for i in vowels if i.grapheme == phoneme] == [0]:
        return True
    else:
        return False

def isRounded(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is rounded.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.rounding for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isClose(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a close vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.mandible for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isCloseMid(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a close-mid vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.mandible for i in vowels if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False

def isOpenMid(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a open-mid vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.mandible for i in vowels if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False

def isOpen(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a open vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.mandible for i in vowels if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False

def isFront(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a front vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.tongue for i in vowels if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isCentral(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a central vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.tongue for i in vowels if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False

def isBack(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a back vowel.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.tongue for i in vowels if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False

def isConsonant(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if phoneme in [i.grapheme for i in consonants]:
        return True
    else:
        return False

def isPlosive(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a plosive consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """
    if [i.manner for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isNasal(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a nasal consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False

def isTrill(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a trilled consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False

def isTaporFlap(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a tapped or flapped consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False

def isFricative(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a fricative consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [5]:
        return True
    else:
        return False

def isLateralFricative(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a lateral consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [6]:
        return True
    else:
        return False

def isApproximant(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is an approximant consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [7]:
        return True
    else:
        return False

def isLateralApproximant(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a lateral approximant consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.manner for i in consonants if i.grapheme == phoneme] == [8]:
        return True
    else:
        return False

def isBilabial(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a bilabial consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isLabiodental(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a labiodental consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [2]:
        return True
    else:
        return False

def isDental(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a dental consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [3]:
        return True
    else:
        return False

def isAlveolar(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is an alveolar consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [4]:
        return True
    else:
        return False

def isPostalveolar(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a postalveolar consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [5]:
        return True
    else:
        return False

def isRetroflex(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a retroflex.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [6]:
        return True
    else:
        return False

def isPalatal(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a palatal consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [7]:
        return True
    else:
        return False

def isVelar(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a velar consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [8]:
        return True
    else:
        return False

def isUvular(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is an uvular consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [9]:
        return True
    else:
        return False

def isPharyngeal(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a pharyngeal consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [10]:
        return True
    else:
        return False

def isGlottal(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is a glottal consonant.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.place for i in consonants if i.grapheme == phoneme] == [11]:
        return True
    else:
        return False

def isVoiced(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is voiced.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.voicing for i in consonants if i.grapheme == phoneme] == [1]:
        return True
    else:
        return False

def isVoiceless(phoneme: str):
    """It takes a phoneme as a grapheme value and checks if it is voiceless.

    Args:
        phoneme (str): The phoneme you need to check

    Returns:
        bool: True if the phoneme has the feature; otherwise, False
    """

    if [i.voicing for i in consonants if i.grapheme == phoneme] == [0]:
        return True
    else:
        return False

def isInitialWord(syllableCounter: int, phonemeCounter: int):
    """It takes the counts of syllables and phonemes and returns if it's on the initial position of the word.

    Args:
        syllableCounter (int): The count of the syllable
        phonemeCounter (int): The count of the phoneme

    Returns:
        bool: True if it's on the initial position of the word; otherwise, False
    """
    
    if syllableCounter == 1 and phonemeCounter == 1:
        return True
    else:
        return False

def isFinalWord(syllableCounter: int, phonemeCounter: int, seq: list):
    """It takes the counts of syllables and phonemes, and the sequence and returns if it's on the final position of the word.

    Args:
        syllableCounter (int): The count of the syllable
        phonemeCounter (int): The count of the phoneme
        seq (list): The sequence of the word

    Returns:
        bool: True if it's on the final position of the word; otherwise, False
    """

    length = 0
    for syl in seq:
        length += len(syl)
    currentIndex = tools.findMyIndex(syllableCounter, phonemeCounter, seq)
    if length - 1 == currentIndex:
        return True
    else:
        return False

def getTongueSyllable(syllable: str):
    """It takes the syllable and returns if it has front or back vowels.

    Args:
        syllable (str): The syllable you need to snalyze

    Returns:
        list: The tongue values of the vowels in the syllable
    """

    for phoneme in syllable:
        if isVowel(phoneme):
            feature = [i.tongue for i in vowels if i.grapheme == phoneme][0]
    return feature