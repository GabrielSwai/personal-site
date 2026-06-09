# =====================================================================================
# Last modification: 2026/06/09
#
# This script automatically parses tone sequences from phrases with diacritics.
# =====================================================================================


# Function:     parse_phrases
# Inputs:       raw_phrases | multiline input phrases (str)
#               default_tone | default tone for vowels with no diacritic (str)
# Outputs:      parsed_phrases | list of annotation intervals and labels from the specified tier (list[dict])
# Description:  Separates a multiline string of phrases by phrase and parses them with parse_tones().

def parse_phrases(raw_phrases, default_tone):
    phrases = [
        line.strip()
        for line in raw_phrases.splitlines()
        if line.strip()
    ]

    parsed_phrases = []

    for phrase in phrases:
        tone_sequence = parse_tones(
            phrase=phrase,
            default_tone=default_tone
        )

        parsed_phrases.append({
            "phrase": phrase,
            "tone_sequence": tone_sequence,
        })

    return parsed_phrases


# Function:     parse_tones
# Inputs:       phrase | input phrases (str)
#               default_tone | default tone for vowels with no diacritic (str)
# Outputs:      tones | parsed tone sequence (str)
# Description:  Takes an input phrase with diacritics and produces the surface tone pattern.

def parse_tones(phrase, default_tone):
    DEFAULT_VOWEL_LIST = ["i", "ɨ", "ʉ", "ɯ", "u", "ɪ", "ʏ", "ʊ", "e", "ø", "ɘ", "ɵ", "ɤ", "o", "ə", "ɛ", "œ", "ɜ", "ɞ", "ʌ", "ɔ", "æ", "ɐ", "a", "ɶ", "ä", "ɑ", "ɒ",
                          "ọ", "ẹ"]
    H_VOWEL_LIST = ["á", "é", "í", "ó", "ú"]
    L_VOWEL_LIST = ["à", "è", "ì", "ò", "ù"]
    F_VOWEL_LIST = ["â", "ê", "î", "ô", "û", "ȃ", "ȇ", "ȋ", "ȏ", "ȗ"]
    R_VOWEL_LIST = ["ǎ", "ě", "ǐ", "ǒ", "ǔ", "ă", "ĕ", "ĭ", "ŏ", "ŭ"]

    tones = ""

    for i in range(len(phrase.lower())):
        char = phrase.lower()[i]

        if char == " ":
            tones = tones[0:len(tones)-1]
            tones += " "

        for vowel in H_VOWEL_LIST:
            if char == vowel:
                tones += "H-"

        for vowel in L_VOWEL_LIST:
            if char == vowel:
                tones += "L-"

        for vowel in F_VOWEL_LIST:  
            if char == vowel:
                tones += "HL-"

        for vowel in R_VOWEL_LIST:  
            if char == vowel:
                tones += "LH-"

        if i+1 < len(phrase):
            next_char = phrase[i+1]
        
        else:
            continue
        
        if next_char == "́":
            tones += "H-"
        
        elif next_char == "̀":
            tones += "L-"
        
        elif next_char == "̄":
            tones += "M-"
        
        elif next_char == "̂":
            tones += "HL-"
        
        elif next_char == "̌":
            tones += "LH-"
        
        else:
            for vowel in DEFAULT_VOWEL_LIST:
                if char == vowel:
                    tones += f"{default_tone}-"


    tones = tones[0:len(tones)-1]

    return tones