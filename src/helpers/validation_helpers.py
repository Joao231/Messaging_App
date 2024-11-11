import re

def validate_message_content(content):
    if not content or not content.strip():
        return False, "Message cannot be empty or whitespace only."
    if len(content) > 500:
        return False, "Message cannot exceed 500 characters."
    if re.search(r'[<>{}*~]', content):
        return False, "Message contains invalid characters."
    return True, ""
