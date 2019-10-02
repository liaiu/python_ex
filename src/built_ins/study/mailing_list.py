from collections import defaultdict
from src.built_ins.study.mail import send_email

class MailingList:

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        return {e for (e,g) in self.email_map.items() if g & groups}

    def send_mailing(self, subject, message, from_addr, *groups, **kwargs):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, **kwargs)

m = MailingList()
m.add_to_group("friend1@example.com", "friends")
m.add_to_group("friend2@example.com", "friends")
m.add_to_group("family1@example.com", "family")
m.add_to_group("pro1@example.com", "professional")
m.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends", "family", headers={"Reply-To": "me2@example.com"})