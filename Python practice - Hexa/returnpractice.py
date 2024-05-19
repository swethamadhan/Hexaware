s_username ="Swe"
s_password ="1234"

username = input("Enter a username: ")
password = input("Enter a password: ")

def validate():
    if(username == s_username and password == s_password):
        return True
    else:
        return False

a=validate()
print(a)
