from services.pdf_service import extract_text_from_pdf

text = extract_text_from_pdf("uploads/resume (8).pdf")

print(text)