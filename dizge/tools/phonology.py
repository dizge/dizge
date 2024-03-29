# -*- coding: utf-8 -*-

import dizge.competence.phonology as phonology
import dizge.competence.lexicon as lexicon

# NORMALIZATION
normalizationChars = {
    "!": "",
    '"': "",
    "#": "",
    "$": "",
    "%": "",
    "&": "",
    "\\": "",
    "'": "",
    "(": "",
    ")": "",
    "*": "",
    "+": "",
    ",": "",
    "-": "",
    ".": "",
    "/": "",
    ":": "",
    ";": "",
    "<": "",
    "=": "",
    ">": "",
    "?": "",
    "@": "",
    "[": "",
    "\\": "",
    "]": "",
    "^": "",
    "_": "",
    "`": "",
    "{": "",
    "|": "",
    "}": "",
    "~": ""
}

loanSignals = {
    "â": "a",
    "ê": "e",
    "î": "i",
    "ô": "ö",
    "û": "ü"
}

def softG(word: str):
    """It takes a word as a string and returns its phonological form with the <ğ> effects.

    Args:
        word (str): The word you want to see the <ğ> effects on

    Returns:
        str: The final form of the input with the <ğ> effects
    """
    softGCount = word.count("ğ")
    i = 0
    word2 = word

    while i < softGCount:
        indexSoftG = word2.index("ğ", 1)
        final = 1 if word2[-1] == "ğ" else 0

        previousP = indexSoftG - 1
        nextP = indexSoftG + 1

        if final == 1:
            word2 = word2.replace("ğ", "\u02D0", 1)
        elif "yığıl" in word2:
            word2 = word2.replace("yığıl", "yıoul", 1)
        elif phonology.isVowel(word2[previousP]) and phonology.isVowel(word2[nextP]):
            if (phonology.isUnrounded(word2[previousP]) and phonology.isFront(word2[previousP])) and (
                    phonology.isUnrounded(word2[nextP]) and phonology.isFront(word2[nextP])):
                word2 = word2.replace("ğ", "y", 1)
            elif word2[previousP] == word2[nextP]:
                word2 = word2.replace("ğ", "\u02D0", 1)
                word2 = word2[:nextP] + word2[nextP + 1:]
            elif word2[previousP] != word2[nextP]:
                word2 = word2.replace("ğ", "\u02D0", 1)
        elif phonology.isVowel(word2[previousP]) and phonology.isConsonant(word2[nextP]):
            if phonology.isUnrounded(word2[previousP]) and phonology.isFront(word2[previousP]):
                word2 = word2.replace("ğ", "y", 1)
            else:
                word2 = word2.replace("ğ", "\u02D0", 1)

        i += 1

    return word2

def normalize(word: str, mode: str = "human"):
    """It takes a word and normalizes it before any linguistic processes.

    Args:
        word (str): The word you need to normalize
        mode (str, optional): If you don't work on any contributing projects for Dizge, please pass it.

    Returns:
        tuple: Normalized form of the input, Loan word signals, The copy of the original input
    """
    loanAlert = 0
    word1 = word.strip().lower().replace(" ", "")
    word2 = ""
    for letter in word1:
        if letter in normalizationChars.keys():
            word2 += normalizationChars[letter]
        else:
            word2 += letter

    word3 = ""
    for letter in word2:
        if letter in loanSignals.keys():
            word3 += loanSignals[letter]
            loanAlert = 1
        else:
            word3 += letter

    output = word3
    if "ğ" in word3 and mode == "machine":
        output = softG(word3)

    if phonology.isConsonant(output[0]) and phonology.isConsonant(output[1]):
        if phonology.isFront(output[2]):
            output = output[0] + "i" + output[1:]
        else:
            output = output[0] + "ı" + output[1:]
            

    return output, loanAlert, word

# SYLLABLE ANALYZER
def syllable_o(word: str, mode: str ="human"):
    """It takes a word and syllabize it based on ortoghrapy.

    Args:
        word (str): The word you need to syllabize
        mode (str, optional): If you don't work on any contributing projects for Dizge, please pass it.

    Returns:
        list: The syllables of the input
    """

    vowels = ["a", "\u0251", "e", "\u025B", "\u0069", "I", "\u0268", "o", "\u0254", "\u00F8", "\u0153", "u", "U", "Y",
              "y"]

    def word2pattern(syl: str):
        """It takes a word and returns the pattern of vowels and consonants in the word.

        Args:
            syl (str): The syllable you need to analyze

        Returns:
            str: The pattern of vowels and consonants
        """

        seq = ""
        for phoneme in syl:
            if phoneme in vowels:
                seq += "V"
            else:
                seq += "C"
        if "VV" in seq:
            seq = seq.replace("VV", "V")
        return seq

    seq = list(normalize(word, mode)[0])
    for i in range(len(seq) - 1, -1, -1):
        if seq[i] in [v.grapheme for v in phonology.vowels]:
            if (i - 1) <= 0:
                continue
            elif seq[i - 1] in [v.grapheme for v in phonology.vowels]:
                continue
            else:
                seq[i - 1] = "." + seq[i - 1]

    analyzedWord = "".join(seq)

    if "." in analyzedWord:
        analyzedWord = analyzedWord.split(".")
    else:
        analyzedWord = [analyzedWord]

    if phonology.isConsonant(word[0]) and phonology.isConsonant(word[1]):
        analyzedWord[1] = word[0] + analyzedWord[1]
        analyzedWord.pop(0)

    if mode == "machine":
        analyzedWord_seq = [word2pattern(syl) for syl in analyzedWord]

    if mode == "machine":
        return list(zip(analyzedWord, analyzedWord_seq))
    else:
        return analyzedWord


def syllable_p(word: str):
    """It takes a word and returns its syllables based on phonology.

    Args:
        word (str): The word you need to syllabize

    Returns:
        list: The syllables of the input (with their phonological patterns)
    """

    vowels = ["a", "\u0251", "e", "\u025B", "\u0069", "I", "\u0268", "o", "\u0254", "\u00F8", "\u0153", "u", "U", "Y",
              "y"]

    def word2pattern(syl: str):
        """It takes a word and returns the pattern of vowels and consonants in the word.

        Args:
            syl (str): The syllable you need to analyze

        Returns:
            str: The pattern of vowels and consonants
        """

        if "d\u0292" in syl:
            syl = syl.replace("d\u0292", "1")
        elif "t\u0283" in syl:
            syl = syl.replace("t\u0283", "2")
        elif "z\u0325" in syl:
            syl = syl.replace("z\u0325", "3")

        seq = ""
        for phoneme in syl:
            if phoneme in vowels:
                seq += "V"
            elif phoneme == "\u02D0" or phoneme == "\u02B0":
                continue
            else:
                seq += "C"
        if "VVV" in seq:
            seq = seq.replace("VVV", "V")
        elif "VV" in seq:
            seq = seq.replace("VV", "V")
        return seq

    if isinstance(g2p(word), str):
        output = g2p(word)
    else:
        output = g2p(word)[0]

    if "d\u0292" in output:
        output = output.replace("d\u0292", "1")
    elif "t\u0283" in output:
        output = output.replace("t\u0283", "2")
    elif "p\u02B0" in output:
        output = output.replace("p\u02B0", "3")
    elif "t\u02B0" in output:
        output = output.replace("t\u02B0", "4")
    elif "k\u02B0" in output:
        output = output.replace("k\u02B0", "5")
    elif "c\u02B0" in output:
        output = output.replace("c\u02B0", "6")

    seq = list(output)

    for i in range(len(seq) - 1, -1, -1):
        if seq[i] in vowels:
            if (i - 1) <= 0:
                continue
            elif seq[i - 1] in vowels or seq[i - 1] == "\u02D0" or seq[i - 1] == "\u02B0":
                continue
            else:
                seq[i - 1] = "." + seq[i - 1]

    analyzedWord = "".join(seq)

    if "1" in analyzedWord:
        analyzedWord = analyzedWord.replace("1", "d\u0292")
    elif "2" in analyzedWord:
        analyzedWord = analyzedWord.replace("2", "t\u0283")
    elif "3" in analyzedWord:
        analyzedWord = analyzedWord.replace("3", "p\u02B0")
    elif "4" in analyzedWord:
        analyzedWord = analyzedWord.replace("4", "t\u02B0")
    elif "5" in analyzedWord:
        analyzedWord = analyzedWord.replace("5", "k\u02B0")
    elif "6" in analyzedWord:
        analyzedWord = analyzedWord.replace("6", "c\u02B0")

    if "." in analyzedWord:
        analyzedWord = analyzedWord.split(".")
    else:
        analyzedWord = [analyzedWord]

    analyzedWord_seq = [word2pattern(syl) for syl in analyzedWord]

    return list(zip(analyzedWord, analyzedWord_seq))


def findMyIndex(syllableCounter: int, phonemeCounter: int, seq: list):
    """It takes syllable and phoneme counts and the sylable piece and returns of the position of the unit.

    Args:
        syllableCounter (int): Which syllable of the word
        phonemeCounter (int): Which phoneme of the syllable
        seq (list): The word sequence

    Returns:
        int: The index of the phoneme
    """

    total = 0
    n = 0
    while n < (syllableCounter - 1):
        total += len(seq[n])
        n += 1
    total += phonemeCounter
    return (total - 1)


def g2p(word: str):
    """It takes a word and returns its phonological transcription

    Args:
        word (str): The word you need to transcribe

    Returns:
        str: The transcription of the input (if there are any alternatives, it may returns a tuple)
    """

    if "zs" in word:
        word = word.replace("zs", "ss")
    word = normalize(word)[0]
    syllables = syllable_o(softG(word), "machine")
    seq = [syllable[0] for syllable in syllables]
    syllableCounter = 0
    phonemeCounter = 0
    output = ""
    alternative = ""
    for syl in seq:
        syllableCounter += 1

        for phoneme in syl:
            phonemeCounter += 1

            if phoneme == "\u02D0":
                output += "\u02D0"

            elif phoneme == "\u02D0":
                output += "\u02D0"

            elif phoneme == "p":
                if phonology.isInitialWord(syllableCounter, phonemeCounter):
                    output += "p\u02B0"
                else:
                    output += "p"

            elif phoneme == "b":
                output += "b"

            elif phoneme == "t":
                if phonology.isInitialWord(syllableCounter, phonemeCounter):
                    output += "t\u02B0"
                else:
                    output += "t"

            elif phoneme == "d":
                output += "d"

            elif phoneme == "k":
                if phonology.getTongueSyllable(syl) == 1:
                    output += "c"
                else:
                    output += "k"
                if phonology.isInitialWord(syllableCounter, phonemeCounter):
                    output += "\u02B0"

            elif phoneme == "g":
                if phonology.getTongueSyllable(syl) == 1:
                    output += "\u025F"
                else:
                    output += "g"

            elif phoneme == "f":
                output += "f"

            elif phoneme == "v":
                if phonology.isInitialWord(syllableCounter, phonemeCounter) == False and phonology.isFinalWord(syllableCounter,
                                                                                               phonemeCounter,
                                                                                               seq) == False:
                    indexV = findMyIndex(syllableCounter, phonemeCounter, seq)
                    previousP = indexV - 1
                    nextP = indexV + 1
                    if phonology.isVowel(word[previousP]) and phonology.isVowel(word[nextP]):
                        output += "\u028B"
                    else:
                        output += "v"
                else:
                    output += "v"

            elif phoneme == "s":
                output += "s"

            elif phoneme == "z":
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq):
                    output += "z\u0325"
                else:
                    output += "z"

            elif phoneme == "ş":
                output += "\u0283"

            elif phoneme == "j":
                output += "\u0292"

            elif phoneme == "ç":
                output += "t\u0283"

            elif phoneme == "c":
                output += "d\u0292"

            elif phoneme == "h":
                if phonology.getTongueSyllable(syl) == 1:
                    output += "ç"
                else:
                    output += "x"

            elif phoneme == "y":
                output += "j"

            elif phoneme == "m":
                output += "m"

            elif phoneme == "n":
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq):
                    output += "n"
                else:
                    indexN = findMyIndex(syllableCounter, phonemeCounter, seq)
                    nextN = indexN + 1
                    if word[nextN] in ["v", "f", "k"] and word in ["cankurtaran", "enfes", "erkenvarmak", "envanter"]:
                        output += "\u0271"
                    elif word[nextN] in ["k", "g"] and word not in ["cankurtaran", "enfes", "erkenvarmak", "envanter"]:
                        output += "\u014B"
                    else:
                        output += "n"

            elif phoneme == "r":
                if phonology.isInitialWord(syllableCounter, phonemeCounter):
                    output += "r"
                elif phonology.isFinalWord(syllableCounter, phonemeCounter, seq):
                    output += "\u0263"
                else:
                    output += "\u027e"

            elif phoneme == "l":
                if phonology.getTongueSyllable(syl) == 1 or (
                        phonology.getTongueSyllable(syl) == 3 and phonology.isInitialWord(syllableCounter, phonemeCounter)):
                    output += "l"
                elif word == "gol":
                    output += "l"
                else:
                    output += "\u0142"

            elif phoneme == "a":
                output += "\u0251"

            elif phoneme == "e":
                if "kendi" in word or "belki" in word:
                    output += "\u025B"
                elif word.count(phoneme) > 1 and not ("kendi" in word or "belki" in word):
                    if output.count("e") > 0:
                        output += "\u025B"
                    else:
                        output += "e"
                else:
                    if syllableCounter > 1 or len(seq) == 1:
                        output += "\u025B"
                    else:
                        output += "e"

            elif phoneme == "o":
                indexO = findMyIndex(syllableCounter, phonemeCounter, seq)
                nextO = indexO + 1
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
                    if word[nextO] == "ğ":
                        output += "o"
                    else:
                        output += "\u0254"
                else:
                    output += "\u0254"

            elif phoneme == "ö":
                if "öğe" in word or "öğü" in word or "öğr" in word or "öğl" in word or "öğm" in word:
                    output += "\u00F8"
                else:
                    output += "\u0153"

            elif phoneme == "i":
                indexİ = findMyIndex(syllableCounter, phonemeCounter, seq)
                nextİ = indexİ + 1
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
                    if word[nextİ] == "ğ":
                        output += "\u0069"
                    else:
                        output += "I"
                else:
                    output += "I"

            elif phoneme == "ı":
                output += "\u0268"

            elif phoneme == "u":
                indexU = findMyIndex(syllableCounter, phonemeCounter, seq)
                nextU = indexU + 1
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
                    if word[nextU] == "ğ":
                        output += "u"
                    else:
                        output += "U"
                else:
                    if softG(word)[-1] == "\u02D0":
                        output += "U"
                    else:
                        output += "u"

            elif phoneme == "ü":
                indexÜ = findMyIndex(syllableCounter, phonemeCounter, seq)
                nextÜ = indexÜ + 1
                if phonology.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
                    if word[nextÜ] == "ğ":
                        output += "y"
                    else:
                        output += "Y"
                else:
                    output += "Y"

        phonemeCounter = 0
    syllableCounter = 0

    if "eğ" in word and "ejI" not in output:
        alternative = output
        alternative = alternative.replace("ej", "\u025B\u02D0I")
    elif "ejI" in output:
        alternative = output
        alternative = alternative.replace("ejI", "\u025B\u02D0I")
    elif "\u025Bj" in output:
        output = output.replace("\u025Bj", "\u025B\u02D0I")
    elif word.startswith("yığıl"):
        output = output.replace("j\u0268\u0254U\u0142", "j\u0268\u02D0o\u02D0U\u0142")
    else:
        if "\u0251j" in output and "mayo" not in word:
            output = output.replace("\u0251j", "\u0251\u02D0I")

        if "ijɛ" in output:
            output = output.replace("ijɛ", "I\u02D0\u025B")
        elif "ij" in output:
            output = output.replace("ij", "i\u02D0")
        elif "Ij" in output and "yy" not in word:
            output = output.replace("Ij", "i\u02D0")

        if "\u0254j" in output:
            output = output.replace("\u0254j", "o\u02D0I")

        if "\u0153j" in output:
            output = output.replace("\u0153j", "\u00F8\u02D0I")

        if "Uj" in output:
            output = output.replace("Uj", "U\u02D0I")

    if "\u0251x\u0251" in output:
        alternative = output
        alternative = alternative.replace("\u0251x\u0251", "\u0251\u02D0")
    elif "x\u0251n\u025B" in output:
        alternative = output
        alternative = alternative.replace("x\u0251n\u025B", "\u0251\u02D0n\u025B")
    elif "kahve" in word:
        alternative = output
        alternative = alternative.replace("\u0251xv", "\u0251\u02D0v")

    if output[-1] == "i":
        output = output[:-1] + "I"

    if output[-1] == "u":
        output = output[:-1] + "U"

    for loan in lexicon.loans.keys():
        if word.startswith(loan):
            output = [ph for ph in output]
            for change in lexicon.loans[loan]:
                output[change[1]] = change[0]
            output = "".join(output)

    if alternative != "":
        return output, alternative
    else:
        return output


def harmony(word: str):
    """It takes a word and returns if the word has vowel harmonies.

    Args:
        word (str): The word you need to check its vowel harmonies
    
    Returns:
        tuple: The e-type vowel harmony, The i-type vowel harmony
    """

    def harmonyOne(word: str):
        """It takes a word and returns if the word has e-type vowel harmony.

        Args:
            word (str): The word you need to check its e-type vowel harmony
        
        Returns:
            bool: The e-type vowel harmony
        """
        
        pattern = []
        for phoneme in word:
            if phonology.isBack(phoneme):
                pattern += "B"
            elif phonology.isFront(phoneme):
                pattern += "F"
            else:
                continue
        if "B" in pattern and "F" in pattern:
            return False
        else:
            return True

    def harmonyTwo(word):
        """It takes a word and returns if the word has i-type vowel harmony.

        Args:
            word (str): The word you need to check its i-type vowel harmony
        
        Returns:
            bool: The i-type vowel harmony
        """

        result = True

        pattern = []
        for phoneme in word:
            if phonology.isVowel(phoneme):
                pattern += phoneme
            else:
                continue

        idxList = []
        for idx in range(len(pattern) - 1):
            idxList.append([idx, idx + 1])

        for i in idxList:
            if phonology.isUnrounded(pattern[i[0]]) and phonology.isUnrounded(pattern[i[1]]):
                result = True
            elif phonology.isRounded(pattern[i[0]]) and ((phonology.isRounded(pattern[i[1]]) and phonology.isClose(pattern[i[1]])) or (
                    phonology.isUnrounded(pattern[i[1]]) and phonology.isOpen(pattern[i[1]]))):
                result = True
            else:
                result = False
                break

        return result

    return (harmonyOne(word), harmonyTwo(word))


def countSyllable(word: str):
    """It takes a word and returns the counts of syllable patterns in the word.

    Args:
        word (str): The word you need to analyze

    Returns:
        dict: The patterns and their counts
    """

    seq = syllable_p(word)
    patterns = {}
    for pattern in seq:
        if pattern[1] not in patterns.keys():
            patterns[pattern[1]] = 0
    for pattern in seq:
        patterns[pattern[1]] += 1
    return patterns