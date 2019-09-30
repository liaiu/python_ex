# asoc unui grup vor fi mai multe roluri
from src.exceptions.rbac_ex.role import SSRole, UsrRole, Role, RoleFactory
from src.exceptions.rbac_ex.role import InvalidAccessZoneException, InvalidAccessLevelException
from src.exceptions.rbac_ex.user import User


class AuthGroup:

    def __init__(self, gr_name):
        self.gr_name = gr_name
        self.role_ss = SSRole("read")
        self.role_usr = UsrRole(None)
        self.users = []

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

    def add_user(self, user):
        self.users.append(user)

    def remove_users(self, user):
        user = self.users.pop(self.users.index(user))
        del user




gr_manager = AuthGroup("manager_group")
gr_manager.changeRole("users", "manage")
gr_manager.changeRole("smartsheet", "manage")
read_only_gr = AuthGroup("Read only gr")
admin_gr = AuthGroup("Admin gr")
admin_gr.changeRole("users", "write")
admin_gr.changeRole("smartsheet", "manage")


usr1 = User("ss_manager", "pass", gr_manager)
print(gr_manager.users)
print("8"*3)

usr2 = User("ss_manager", "pass", gr_manager)
# print(gr_manager.users)
# print("^"*30)
# gr_manager.remove_users(usr2)
# print(gr_manager.users)





#
# while True:
#     try:
#         zone = input("Choose zone form: {}".format(Role.acc_zones))
#         acc_lvl = input("Choose acc lvl from: {}".format(RoleFactory.getRole(zone).aceess_levels))
#         g.changeRole(zone, acc_lvl)
#     except InvalidAccessLevelException:
#         print("Enter the correct access level again")
#     except InvalidAccessZoneException:
#         print("Enter the correct zone again")
#     else:
#         break
