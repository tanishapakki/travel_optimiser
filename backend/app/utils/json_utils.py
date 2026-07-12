
import re

def strip_markdown_fences(text:str) -> str:

    text =text.strip()

    pattern = r"^```(?:json)?\s*(.*?)\s*```$"

    match= re.match(pattern,text, re.DOTALL | re.IGNORECASE)

    if match:
        return match.group(1).strip()
    
    return text