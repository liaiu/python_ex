# read/write/manage
# users/ smartsheet


#3 types: admin/ guest/ contributor

class Role:
    aceess_levels = ["read", "write", "manage", None]
    acc_zones = ["smartsheet", "users"]

    def __init__(self, access_level, access_zone):
        self._access_level = access_level
        self.access_zone = access_zone

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, new_lvl):
        if new_lvl not in self.aceess_levels:
            raise InvalidAccessLevelException("Access levels valid are: {}".format(self.aceess_levels))
        else:
            self._access_level = new_lvl

    def __repr__(self):
        return "Zone: {} - {}".format(self.access_zone, self.access_level)


class SSRole(Role):
    aceess_levels = ["read", "write", "manage"]

    def __init__(self, acces_level):
        super(SSRole, self).__init__(access_level=acces_level, access_zone="smartsheet")


class UsrRole(Role):

    def __init__(self, aceess_level):
        super(UsrRole, self).__init__(access_level=aceess_level, access_zone="users")

class RoleFactory:

    @classmethod
    def getRole(self, acc_zone, acc_lvl="read"):
        if acc_zone == "smartsheet":
            return SSRole(acc_lvl)
        if acc_zone == "users":
            return UsrRole(acc_lvl)
        raise InvalidAccessZoneException

class InvalidAccessLevelException(Exception):

    pass


class InvalidAccessZoneException(Exception):

    pass