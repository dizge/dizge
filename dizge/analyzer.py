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


import dizge.tools as tp


def standardize(data, preference=1):
    """

    :param data:
    :param preference:
    :return:
    """
    if isinstance(data, str):
        splittedText = data.split()
        normalizedText = [tp.normalize(word) for word in splittedText]
    else:
        normalizedText = [tp.normalize(word) for word in data]

    normalizedWords = [word[0] for word in normalizedText]
    loanSignals = [word[1] for word in normalizedText]
    originalWords = [word[2] for word in normalizedText]

    if preference == 1:
        return normalizedWords
    elif preference == 2:
        return loanSignals
    elif preference == 3:
        return originalWords
    else:
        return "ERROR: Your preference isn't an option!"


def analyze(data, mode):
    """
    araçlardan bir veya birkaçını bir veri seti üzerinde tek seferde analiz etmek ve bütüncül bir çıktı almak için
    `analyzer` modülü içindeki `analyze()` fonksiyonunu kullanabilirsiniz. Bu fonksiyon ilki verinin kendisi,
    ikincisi de istediğiniz araçların adlarından oluşan bir liste olmak üzere iki zorunlu parametreden oluşmaktadır.

    >>> from dizge.analyzer import analyze
    >>> data = pd.read_csv("../data/testset_v4.0.csv", sep=";", index_col="ID")
    >>> words = standardize(data["word"])

    >>> result = analyze(words, ["g2p", "harmony"])

    >>> result.to_csv("testset_v4.0.csv", sep=";", encoding="utf-8-sig")

    :param data: Analiz edilmek istenen csv dosyası
    :param mode: kullanmak istenilen aracın adı
    :return: csv dosyası
    """
    dict = {
            'word': data
            }
    if "g2p" in mode:
        result = [tp.g2p(word) for word in data]
        dict["g2p"] = result
    if "syllable_o" in mode:
        result = [tp.syllable_o(word) for word in data]
        dict["syllable_o"] = result
    if "syllable_p" in mode:
        result = [tp.syllable_p(word) for word in data]
        dict["syllable_p"] = result
    if "countSyllable" in mode:
        result = [tp.countSyllable(word) for word in data]
        dict["countSyllable"] = result
    if "harmony" in mode:
        result = [tp.harmony(word) for word in data]
        dict["harmony"] = result
    return dict
