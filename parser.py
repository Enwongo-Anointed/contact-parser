import pdfplumber
from models import Contact
from cleaner import normalize_phone

def parse_pdf(file_path):

    contacts = []

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if not text:
                continue

            lines = text.split("\n")

            for line in lines:

                parts = line.split("-")

                if len(parts) < 2:
                    continue

                name = parts[0].strip()
                phone = parts[1].strip()

                note = ""
                if len(parts) > 2:
                    note = parts[2].strip()

                phone = normalize_phone(phone)

                if phone is None:
                    continue

                contact = Contact(name=name, phone=phone, note=note)

                contacts.append(contact)

    return contacts