class Message:
    def __init__(self, sender_id, content, timestamp, message_type, group_id=None, is_read=None):
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp
        self.message_type = message_type
        self.group_id = group_id
        self.is_read = is_read if is_read is not None else {}
        
    def to_dict(self):
        return {
            "sender_id": self.sender_id,
            "content": self.content,
            "timestamp": self.timestamp,
            "type": self.message_type,
            "group_id": self.group_id,
            "is_read": self.is_read
        }
