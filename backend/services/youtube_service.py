from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def get_video_id(url: str):
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]

    return None


def extract_transcript(url: str):
    video_id = get_video_id(url)

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id, languages=["hi", "en"])

    text = ""

    for snippet in transcript:
        text += snippet.text + " "

    return text
