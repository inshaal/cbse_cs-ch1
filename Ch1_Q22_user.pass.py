#made by Gm Harshvardhan
#To input username&pass and check if it's correct. Q22
u=[]
p=[]
count=input("Enter number of usernames you want to save : ")
for i in range(0, count):
    username=raw_input("Enter username to save : ")
    password=raw_input("Enter password to save : ")
    position_user=len(u)+1
    position_pass=len(p)+1
    u.append(username)
    p.append(password)
#Search function begins
def passcheck():
    user_=raw_input("Enter username to log in : ")
    pass_=raw_input("Ente password to log in : ")
    if user_ in u:
        if pass_ in p:
            if position_user==position_pass:
                print "Verified user. "
        else:
            print "Password doesn't match. "
    else:
        print "Username doesn't exist"
passcheck()
