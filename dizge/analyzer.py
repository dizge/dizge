# -*- coding: utf-8 -*-

import dizge.tools as tools

def standardize(data: str, preference: int =1):
    """It takes data and standardizes it before the analysis.

    Args:
        data (str or list): The data you need to analyze
        preference (int, optional): If you don't work on any contributing projects for Dizge, please pass it.

    Returns:
        list: The standardized format of the input
    """
    if isinstance(data, str):
        splittedText = data.split()
        normalizedText = [tools.normalize(word) for word in splittedText]
    else:
        normalizedText = [tools.normalize(word) for word in data]

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

def analyze(data: list, selectedTools: list):
    """It takes data and tools list and runs the selected tools with the given data

    Args:
        data (list): The data you need to analyze
        selectedTools (list): The tools you want to use

    Returns:
        dict: The analyze results
    """
        
    dict = {
            'word': standardize(data)
            }
    if "g2p" in selectedTools:
        result = [tools.g2p(word) for word in data]
        dict["g2p"] = result
    if "syllable_o" in selectedTools:
        result = [tools.syllable_o(word) for word in data]
        dict["syllable_o"] = result
    if "syllable_p" in selectedTools:
        result = [tools.syllable_p(word) for word in data]
        dict["syllable_p"] = result
    if "countSyllable" in selectedTools:
        result = [tools.countSyllable(word) for word in data]
        dict["countSyllable"] = result
    if "harmony" in selectedTools:
        result = [tools.harmony(word) for word in data]
        dict["harmony"] = result
    return dict