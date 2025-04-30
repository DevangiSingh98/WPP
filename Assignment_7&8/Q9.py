import re

def tokenize_malayalam(text):
  
    patterns = {
        "urls": r"https?://\S+|www\.\S+",  
        "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",  
        "dates": r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b",  
        "numbers": r"\b\d{1,3}(,\d{2,3})*\b|\b\d+(\.\d+)?\b",  
        "malayalam_numbers": r"[\u0D66-\u0D6F]+", 
        "social_media": r"[@#][\w]+",  
        "punctuation": r"[\.,!?;:()\[\]{}]",  
        "malayalam_words": r"[\u0D00-\u0D7F]+",  
    }

    tokens = []
    
    
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        tokens.extend(matches)
    
    return tokens

# Example Malayalam text
text = """
ഞാൻ 2025-02-20 ന് 3,22,243 രൂപയ്ക്കു് ഒരു ജാലകം വാങ്ങി.
ഇവിടെ ഒരു വെബ്‌സൈറ്റ് ഉണ്ട്: https://example.com
എന്റെ ഇമെയിൽ: test@example.com
ഫേസ്ബുക്കിൽ എന്നെ ഫോളോ ചെയ്യൂ: @malayalamuser #കേരളം
"""


tokens = tokenize_malayalam(text)
print(tokens)
