import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    return "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )
