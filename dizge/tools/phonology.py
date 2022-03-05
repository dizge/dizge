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

import dizge.competence.phonology as p
import dizge.competence.lexicon as lex

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

def softG(word):
    """

    :param word:
    :return:
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
        elif p.isVowel(word2[previousP]) and p.isVowel(word2[nextP]):
            if (p.isUnrounded(word2[previousP]) and p.isFront(word2[previousP])) and (
                    p.isUnrounded(word2[nextP]) and p.isFront(word2[nextP])):
                word2 = word2.replace("ğ", "y", 1)
            elif word2[previousP] == word2[nextP]:
                word2 = word2.replace("ğ", "\u02D0", 1)
                word2 = word2[:nextP] + word2[nextP + 1:]
            elif word2[previousP] != word2[nextP]:
                word2 = word2.replace("ğ", "\u02D0", 1)
        elif p.isVowel(word2[previousP]) and p.isConsonant(word2[nextP]):
            if p.isUnrounded(word2[previousP]) and p.isFront(word2[previousP]):
                word2 = word2.replace("ğ", "y", 1)
            else:
                word2 = word2.replace("ğ", "\u02D0", 1)

        i += 1

    return word2


def normalize(word, mode="human"):
    """

    :param word:
    :param mode:
    :return:
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

    if p.isConsonant(output[0]) and p.isConsonant(output[1]):
        if p.isFront(output[2]):
            output = output[0] + "i" + output[1:]
        else:
            output = output[0] + "ı" + output[1:]
            

    return output, loanAlert, word


# SYLLABLE ANALYZER
def syllable_o(word, mode="human"):
    """

    :param word:
    :param mode:
    :return:
    """

    vowels = ["a", "\u0251", "e", "\u025B", "\u0069", "I", "\u0268", "o", "\u0254", "\u00F8", "\u0153", "u", "U", "Y",
              "y"]

    def word2pattern(syl):
        """

        :param syl:
        :return:
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
        if seq[i] in [v.grapheme for v in p.vowels]:
            if (i - 1) <= 0:
                continue
            elif seq[i - 1] in [v.grapheme for v in p.vowels]:
                continue
            else:
                seq[i - 1] = "." + seq[i - 1]

    analyzedWord = "".join(seq)

    if "." in analyzedWord:
        analyzedWord = analyzedWord.split(".")
    else:
        analyzedWord = [analyzedWord]

    if p.isConsonant(word[0]) and p.isConsonant(word[1]):
        analyzedWord[1] = word[0] + analyzedWord[1]
        analyzedWord.pop(0)

    if mode == "machine":
        analyzedWord_seq = [word2pattern(syl) for syl in analyzedWord]

    if mode == "machine":
        return list(zip(analyzedWord, analyzedWord_seq))
    else:
        return analyzedWord


def syllable_p(word):
    """

    :param word:
    :return:
    """
    vowels = ["a", "\u0251", "e", "\u025B", "\u0069", "I", "\u0268", "o", "\u0254", "\u00F8", "\u0153", "u", "U", "Y",
              "y"]

    def word2pattern(syl):
        """

        :param syl:
        :return:
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


def findMyIndex(syllableCounter, phonemeCounter, seq):
    """

    :param syllableCounter:
    :param phonemeCounter:
    :param seq:
    :return:
    """
    total = 0
    n = 0
    while n < (syllableCounter - 1):
        total += len(seq[n])
        n += 1
    total += phonemeCounter
    return (total - 1)


def g2p(word):
    word2 = word
    """

    :param word:
    :return:
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
                if p.isInitialWord(syllableCounter, phonemeCounter):
                    output += "p\u02B0"
                else:
                    output += "p"

            elif phoneme == "b":
                output += "b"

            elif phoneme == "t":
                if p.isInitialWord(syllableCounter, phonemeCounter):
                    output += "t\u02B0"
                else:
                    output += "t"

            elif phoneme == "d":
                output += "d"

            elif phoneme == "k":
                if p.getTongueSyllable(syl) == 1:
                    output += "c"
                else:
                    output += "k"
                if p.isInitialWord(syllableCounter, phonemeCounter):
                    output += "\u02B0"

            elif phoneme == "g":
                if p.getTongueSyllable(syl) == 1:
                    output += "\u025F"
                else:
                    output += "g"

            elif phoneme == "f":
                output += "f"

            elif phoneme == "v":
                if p.isInitialWord(syllableCounter, phonemeCounter) == False and p.isFinalWord(syllableCounter,
                                                                                               phonemeCounter,
                                                                                               seq) == False:
                    indexV = findMyIndex(syllableCounter, phonemeCounter, seq)
                    previousP = indexV - 1
                    nextP = indexV + 1
                    if p.isVowel(word[previousP]) and p.isVowel(word[nextP]):
                        output += "\u028B"
                    else:
                        output += "v"
                else:
                    output += "v"

            elif phoneme == "s":
                output += "s"

            elif phoneme == "z":
                if p.isFinalWord(syllableCounter, phonemeCounter, seq):
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
                if p.getTongueSyllable(syl) == 1:
                    output += "ç"
                else:
                    output += "x"

            elif phoneme == "y":
                output += "j"

            elif phoneme == "m":
                output += "m"

            elif phoneme == "n":
                if p.isFinalWord(syllableCounter, phonemeCounter, seq):
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
                if p.isInitialWord(syllableCounter, phonemeCounter):
                    output += "r"
                elif p.isFinalWord(syllableCounter, phonemeCounter, seq):
                    output += "\u0263"
                else:
                    output += "\u027e"

            elif phoneme == "l":
                if p.getTongueSyllable(syl) == 1 or (
                        p.getTongueSyllable(syl) == 3 and p.isInitialWord(syllableCounter, phonemeCounter)):
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
                if p.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
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
                if p.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
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
                if p.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
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
                if p.isFinalWord(syllableCounter, phonemeCounter, seq) == False:
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

    for loan in lex.loans.keys():
        if word.startswith(loan):
            output = [ph for ph in output]
            for change in lex.loans[loan]:
                output[change[1]] = change[0]
            output = "".join(output)

    if alternative != "":
        return output, alternative
    else:
        return output


def harmony(word):
    """

    :param word:
    :return:
    """
    def harmonyOne(word):
        """

        :param word:
        :return:
        """
        pattern = []
        for phoneme in word:
            if p.isBack(phoneme):
                pattern += "B"
            elif p.isFront(phoneme):
                pattern += "F"
            else:
                continue
        if "B" in pattern and "F" in pattern:
            return False
        else:
            return True

    def harmonyTwo(word):
        """

        :param word:
        :return:
        """
        result = True

        pattern = []
        for phoneme in word:
            if p.isVowel(phoneme):
                pattern += phoneme
            else:
                continue

        idxList = []
        for idx in range(len(pattern) - 1):
            idxList.append([idx, idx + 1])

        for i in idxList:
            if p.isUnrounded(pattern[i[0]]) and p.isUnrounded(pattern[i[1]]):
                result = True
            elif p.isRounded(pattern[i[0]]) and ((p.isRounded(pattern[i[1]]) and p.isClose(pattern[i[1]])) or (
                    p.isUnrounded(pattern[i[1]]) and p.isOpen(pattern[i[1]]))):
                result = True
            else:
                result = False
                break

        return result

    return (harmonyOne(word), harmonyTwo(word))


def countSyllable(word):
    """

    :param word:
    :return:
    """
    seq = syllable_p(word)
    patterns = {}
    for pattern in seq:
        if pattern[1] not in patterns.keys():
            patterns[pattern[1]] = 0
    for pattern in seq:
        patterns[pattern[1]] += 1
    return patterns