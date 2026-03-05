def normalize_phone(phone):
    import re
    phone = re.sub(r"\D", "", phone)

    if phone.startswith("+234"):
        return phone

    if phone.startswith("234"):
        return "+" + phone

    if phone.startswith("0"):
        return "+234" + phone[1:]

    return None