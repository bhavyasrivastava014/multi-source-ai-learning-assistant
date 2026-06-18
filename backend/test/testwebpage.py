from services.webpage_service import extract_text_from_url

text = extract_text_from_url("https://bhavya14.vercel.app/")

print(text[:1000])
