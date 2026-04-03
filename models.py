class Contact:
    def __init__(self, name, phone, note):
        self.name = name.strip()
        self.phone = phone.strip()
        self.note = note.strip()
        self.formatted_name = f"{self.name} - {self.note}"

    def __repr__(self):
        return f"{self.formatted_name} | {self.phone}"