def normalize_phone(phone):
    phone = phone.strip().replace(" ", "").replace("-", "")

    if phone.startswith("+234"):
        return phone

    if phone.startswith("234"):
        return "+" + phone

    if phone.startswith("0"):
        return "+234" + phone[1:]

    return None