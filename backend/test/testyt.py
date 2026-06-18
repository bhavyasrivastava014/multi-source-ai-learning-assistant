from services.youtube_service import extract_transcript

text = extract_transcript(
    "https://youtu.be/gm11jFmyxIA?si=r74OYl9NUTTgSXO8"
)

print(text[:1000])