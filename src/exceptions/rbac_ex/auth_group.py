# asoc unui grup vor fi mai multe roluri
from src.exceptions.rbac_ex.role import SSRole, UsrRole, Role, RoleFactory
from src.exceptions.rbac_ex.role import InvalidAccessZoneException, InvalidAccessLevelException


class AuthGroup:

    def __init__(self):
        self.role_ss = SSRole("read")
        self.role_usr = UsrRole(None)

    def changeRole(self, zone_to_modify, acess_level):
        if zone_to_modify == "smartsheet":
            self.role_ss.access_level = acess_level
        elif zone_to_modify == "users":
            self.role_usr.access_level = acess_level
        else:
            raise InvalidAccessZoneException(zone_to_modify)

    def show_roles(self):
        print(self.role_ss)
        print(self.role_usr)


g = AuthGroup()
g.show_roles()
g.changeRole("users", "manage")
g.show_roles()
print("*******")

while True:
    try:
        zone = input("Choose zone form: {}".format(Role.acc_zones))
        acc_lvl = input("Choose acc lvl from: {}".format(RoleFactory.getRole(zone).aceess_levels))
        g.changeRole(zone, acc_lvl)
    except InvalidAccessLevelException:
        print("Enter the correct access level again")
    except InvalidAccessZoneException:
        print("Enter the correct zone again")
    else:
        break
