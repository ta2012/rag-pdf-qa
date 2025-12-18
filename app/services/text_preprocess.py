import re
from typing import List

def normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def normalize_pages(pages: List[str]) -> List[str]:
    return [normalize_text(p) for p in pages]
