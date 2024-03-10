# Dizge: The grammar analyzer for Turkish

![Version](https://img.shields.io/pypi/v/dizge?style=flat-square)
![License](https://img.shields.io/pypi/l/dizge?style=flat-square)

## Table of Contents
1. [Introduction](#introduction)<br>
2. [How to Use](#how-to-use)<br>
2.1. [Installation and First Run](#installation-and-first-run)<br>
2.2. [`competence` Functions](#competence-functions)<br>
2.3. [`tools` Functions](#tools-functions)<br>
2.4. [Data Loading](#data-loading)<br>
2.5. [Analysis and Getting Result](#analysis-and-getting-result)<br>
3. [Contact](#contact)

## Introduction
**Dizge** is an open-source Python project for linguistic analysis of Turkish data. The project consists of two modules:

* `competence`: It represents the linguistic knowledge of an ideal native speaker, and it's programmed in the Object Oriented Programming (OOP) principles.
* `tools`: It includes rule-based functions representing the linguistic processes.

The current version (v0.1.x) of the project has a few phonetic/phonological functions, as a pre-version.

For the theoretical background of **Dizge**, the following resources have benefitted from:

- Ergenç, İ., & Uzun, İ. P. (2020). *Türkçenin ses dizgesi* (2nd ed.). Seçkin Yayınevi.<br/>
- IPA Chart, http://www.internationalphoneticassociation.org/content/ipa-chart, available under a Creative Commons Attribution-Sharealike 3.0 Unported License. Copyright © 2018 International Phonetic Association.

You can cite our project in your publications:<br/>
```
Mutlu, M. U., Yetimaslan, N., & Atagün, İ. (2021). Dizge: The grammar analyzer for Turkish. https://github.com/dizge
```

Also, Dizge has a no-code web service on https://dizge.pythonanywhere.com.

## How to Use
### Installation and First Run
You can use the pip tool to install the package to your system with the following `pip install dizge` command. Then, it's easy to call it in any Python script:

```python
import dizge
```

### `competence` Functions
**Dizge** has all the Turkish phonemes and their linguistic features. For example, you can easily get a list of Turkish vowels and consonants:
```python
for i in [vars(phoneme) for phoneme in dizge.vowels]:
    print(i)

for i in [vars(phoneme) for phoneme in dizge.consonants]:
    print(i)
```

Similarly, you can check if any phonemes have a feature with the help of functions in `competence`.  It's enough to give the grapheme of any phonemes as string inputs to the following functions:

* `isVowel()`: If a phoneme is a vowel, it'll return **True**; otherwise, it'll return **False**.
* `isUnrounded()`: If a phoneme is an unrounded vowel, it'll return **True**; otherwise, it'll return **False**.
* `isRounded()`: If a phoneme is a rounded vowel, it'll return **True**; otherwise, it'll return **False**.
* `isClose()`: If a phoneme is a closed vowel, it'll return **True**; otherwise, it'll return **False**.
* `isCloseMid()`: If a phoneme is a mid-closed vowel, it'll return **True**; otherwise, it'll return **False**.
* `isOpenMid()`: If a phoneme is a mid-open vowel, it'll return **True**; otherwise, it'll return **False**.
* `isOpen()`: If a phoneme is an open vowel, it'll return **True**; otherwise, it'll return **False**.
* `isFront()`: If a phoneme is a front vowel, it'll return **True**; otherwise, it'll return **False**.
* `isCentral()`: If a phoneme is a central vowel, it'll return **True**; otherwise, it'll return **False**.
* `isBack()`: If a phoneme is a back vowel, it'll return **True**; otherwise, it'll return **False**.
* `isConsonant()`: If a phoneme is a consonant, it'll return **True**; otherwise, it'll return **False**.
* `isPlosive()`: If a phoneme is a plosive consonant, it'll return **True**; otherwise, it'll return **False**.
* `isNasal()`: If a phoneme is a nasal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isTrill()`: If a phoneme is a trilled consonant, it'll return **True**; otherwise, it'll return **False**.
* `isTaporFlap()`: If a phoneme is a tapped or flapped consonant, it'll return **True**; otherwise, it'll return **False**.
* `isFricative()`: If a phoneme is a fricative consonant, it'll return **True**; otherwise, it'll return **False**.
* `isLateralFricative()`: If a phoneme is a lateral fricative consonant, it'll return **True**; otherwise, it'll return **False**.
* `isApproximant()`: If a phoneme is an approximantal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isLateralApproximant()`: If a phoneme is a lateral approximantal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isBilabial()`: If a phoneme is a bilabial consonant, it'll return **True**; otherwise, it'll return **False**.
* `isLabiodental()`: If a phoneme is a labiodental consonant, it'll return **True**; otherwise, it'll return **False**.
* `isDental()`: If a phoneme is a dental consonant, it'll return **True**; otherwise, it'll return **False**.
* `isAlveolar()`: If a phoneme is an alveolar consonant, it'll return **True**; otherwise, it'll return **False**.
* `isPostalveolar()`: If a phoneme is a postalveolar consonant, it'll return **True**; otherwise, it'll return **False**.
* `isRetroflex()`: If a phoneme is a retroflex consonant, it'll return **True**; otherwise, it'll return **False**.
* `isPalatal()`: If a phoneme is a palatal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isVelar()`: If a phoneme is a velar consonant, it'll return **True**; otherwise, it'll return **False**.
* `isUvular()`: If a phoneme is an ulvular consonant, it'll return **True**; otherwise, it'll return **False**.
* `isPharyngeal()`: If a phoneme is a pharyngeal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isGlottal()`: If a phoneme is a glottal consonant, it'll return **True**; otherwise, it'll return **False**.
* `isVoiced()`: If a phoneme is voiced, it'll return **True**; otherwise, it'll return **False**.
* `isVoiceless()`: If a phoneme is voiceless, it'll return **True**; otherwise, it'll return **False**.

### `tools` Functions

In this module, there are some functions of linguictic processes, like transcription (Grapheme-to-Phoneme or G2P), syllablization, etc.

First, the `softG()` function shows the effects, such as vowel shifting or lengthening, of the <ğ> grapheme without a phoneme value: 

```python
>>> dizge.softG('dağ')
'daː'
>>> dizge.softG('göğüs')
'göːüs'
>>> dizge.softG('eğlence')
'eylence'
```

We provide two options for syllabilzation analysis. First of them is the orthography-based analysis, as the traditional method. `syllable_o()` works in this way.

```python
>>> dizge.syllable_o('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
['af', 'yon', 'ka', 'ra', 'hi', 'sar', 'lı', 'laş', 'tı', 'ra', 'ma', 'dık', 'la', 'rı', 'mız', 'dan', 'mış', 'ça', 'sı', 'na']
```

However, if you care about the phonetic occurences during the syllablization, you can use the `syllable_p()` function.

```python
>>> dizge.syllable_p('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
[('ɑf', 'VC'), ('jɔŋ', 'CVC'), ('kɑ', 'CV'), ('ɾɑ', 'CV'), ('çI', 'CV'), ('sɑɾ', 'CVC'), ('łɨ', 'CV'), ('łɑʃ', 'CVC'), ('tɨ', 'CV'), ('ɾɑ', 'CV'), ('mɑ', 'CV'), ('dɨk', 'CVC'), ('łɑ', 'CV'), ('ɾɨ', 'CV'), ('mɨz', 'CVC'), ('dɑn', 'CVC'), ('mɨʃ', 'CVC'), ('tʃɑ', 'CV'), ('sɨ', 'CV'), ('nɑ', 'CV')]
```

Also, you can get a comprehensive calculation of the analysis with the `countSyllable()` function:

```python
>>> dizge.countSyllable('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
{'VC': 1, 'CVC': 7, 'CV': 12}
```

You can analyze the vowel harmony of a word, as a signal of Turkish originated words, with the `harmony()` function. It checks e-type and i-type harmonies of the word and returns both in a tuple:

```python
>>> dizge.harmony('ankara')
(True, True)
```

Last but not least, the `g2p()` function transcribes from graphemes to phonemes in a rule-based way:

```python
>>> dizge.g2p('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
'ɑfjɔŋkɑɾɑçIsɑɾłɨłɑʃtɨɾɑmɑdɨkłɑɾɨmɨzdɑnmɨʃtʃɑsɨnɑ'
```

**DISCLAIMER:**

- Unlike our reference resources, we ignored the half-long occurences. It may be implemented in the upcoming updates.
- Also, we provide more than one alternative for the examples our reference resources provide alternatives based on the spoken language. You can pick the one you need by indexing.

### Data Loading
While using **Dizge**, you can work on tabular data in the *xlsx* and *csv* formats or plain-text data in the *txt* format. It's possible to use the 3rd party data processing libraries or built-in Python functions to load the data, based on your choice. Here's an example usage:

```python
data = open('data/sample.txt', 'r', encoding="utf-8").read()
```

After loading the data, you can select the part you need to analyze, and you can standardize the data before starting the analysis. If you prefer to use the `analyze()` function we'll mention in the next section, the function already standardizes your data. Let's look at how to use the `standardize()` function:

```python
words = dizge.standardize(data)
```
 
### Analysis and Getting Result
You can use the `analyze()` function to analyze the data easily. It's enough to give two inputs, i.e.nthe data you work on, and the tools you want to use. That's all:

```python
>>> tools = ["g2p", "syllable_o", "syllable_p", "countSyllable", "harmony"]
>>> result = dizge.analyze(words, tools)
```

## Contact
For any requests about **Dizge**, you can use the following contact info:

**Email:** dizgenlp@gmail.com<br>
**X (formerly Twitter):** [@dizgenlp](https://twitter.com/dizgenlp)<br>
**Instagram:** [@dizgenlp](https://instagram.com/dizgenlp)<br>

Additionally, please feel free to create issue or PRs (pull requests).