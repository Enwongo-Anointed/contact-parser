class Contact:
    def __init__(self, name, phone, description):
        self.name = name.strip()
        self.phone = phone.strip()
        self.description = description.strip()
        self.formatted_name = f"{self.name} - {self.description}"

    def __repr__(self):
        return f"{self.formatted_name} | {self.phone}"