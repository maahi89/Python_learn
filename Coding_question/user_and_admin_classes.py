class user:
    def __init__(self, username,emailid):
        self.username=username
        self.emailid=emailid
    def login(self):
        print(f"{self.username} has logged in")
    def logout(self):
        print(f"{self.username} has logged out")
class admin(user):
    def __init__(self, username,emailid, admi_level):
        self.username=username
        self.emailid=emailid
        # super().__init__(username, emailid)
        self.admi_level=admi_level
    def delete_user(self,username):
        print(f"admin {self.username} deleted user {username.username}")
u=user("mahitha","mah@gmail.com")       
u.login()
u.logout()
a=admin("rahul", "rahul@gmail.com", "Super Admin")
a.login()
a.delete_user(u)

