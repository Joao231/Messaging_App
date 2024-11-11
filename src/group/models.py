from datetime import datetime


class Group:
    def __init__(self, group_name, members=None):
        self.group_name = group_name
        self.members = {username: datetime.utcnow() for username in members} if members else {}

    def to_dict(self):
        return {
            "group_name": self.group_name,
            "members": self.members,
            "created_at": datetime.utcnow()
        }
