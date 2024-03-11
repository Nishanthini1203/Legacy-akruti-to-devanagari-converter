# Akruti to Unicode mapping
akruti_to_unicode = {
    'ç': 'क', 'é': 'ख', 'ü': 'ग', '™': 'घ', '≤': 'ङ',
    'Ä': 'च', 'ï': 'छ', 'ù': 'ज', 'Ë': 'झ', '—': 'ञ',
    '¡': 'ट', '¢': 'ठ', '™': 'ड', '£': 'ढ', '∞': 'ण',
    '¶': 'त', '§': 'थ', '•': 'द', 'ª': 'ध', 'º': 'न',
    'à': 'प', 'á': 'फ', 'â': 'ब', 'ã': 'भ', 'ä': 'म',
    'ç': 'य', 'è': 'र', 'é': 'ल', 'ê': 'ळ', 'ë': 'व',
    'ì': 'श', 'í': 'ष', 'î': 'स', 'ð': 'ह', 'Ï': 'क़',
    'Ü': 'ग़', '¢': 'ज़', '£': 'ड़', 'á': 'फ़', 'Ÿ': 'य़',
    'é': 'ल़', 'ç': 'क्ष', '™': 'ज्ञ', 'é': 'ल्ल', 'È': 'ऋ',
    'à': 'ू', 'á': 'ौ', 'â': 'ृ', 'ã': 'ै', 'ä': 'ॉ',
    'ç': 'ू', 'è': 'ं', 'é': 'ँ', 'ë': 'ः', 'é': 'ए',
    'æ': 'ा', 'ç': '१', 'è': '२', 'é': '३', 'ê': '४',
    'ë': '५', 'ì': '६', 'í': '७', 'î': '८', 'ð': '९',
    'à': '०', 'á': 'ऑ', 'â': 'अं', 'ã': 'औ', 'ä': 'अः',
    'å': 'अँ', 'ç': 'क़ा', 'é': 'ल्ला', 'è': 'रु', 'ë': 'ज़्य'
}

def convert_akruti_to_unicode(akruti_text):
    unicode_text = ''
    for char in akruti_text:
        unicode_text += akruti_to_unicode.get(char, char)
    return unicode_text

