import hashlib
from src.exceptions.rbac_ex.auth_exceptions import UsernameAlreadyExists


class User:
    taken_usernamess = []

    def __init__(self, username, password, auth_group):
        """Create a new user object. The password will be encrypted before storing."""
        if username not in self.taken_usernamess:
            self.username = username
            self.password = self._encrypt_pw(password)
            self.is_logged_in = False
            self.auth_group = auth_group
            self.auth_group.add_user(self)
            self.taken_usernamess.append(username)
        else:
            raise UsernameAlreadyExists(username)

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

    def __del__(self):
        if getattr(self, "username", None):
            self.taken_usernamess.remove(self.username)

    def __repr__(self):
        return """
        Name: {}
        Auth goup: {}
        """.format(self.username, self.auth_group.gr_name)

