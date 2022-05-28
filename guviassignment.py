
user = input('Enter login if register user if not enter register : ')
if user == 'register':
    emailid = input('enter your emailid : ')
    for i in emailid:
        if i=='@' and emailid[emailid.index("@")+1]=='.':
            print("Error please don't  use \".\" after @\nPlease try again")
            break
    else:
        pass
        password = input('ENTER YOUR PASSWORD \nPassword must atleast contain one uppercase\none digit\none lowercase character\none special character\nThe password should be of length of 5 to 15 character  : ')

        special = ['!','@','#','$','%','^','&','*']
        copy = password
        a = 0
        numspec = 0
        upper = 0
        lower = 0
        digit = 0
        while len(copy)>a:
            j=copy[a]
            if j in special:
                numspec += 1
                a += 1
            elif j.isupper():
                upper += 1
                a += 1
            elif j.islower():
                lower += 1
                a+=1
            elif j.isdigit():
                digit += 1
                a += 1

        if numspec==0:
            print("Error there must be atleast one special character in the password.\nPlease try again")
        elif upper==0:
            print('Error : There must be atleast one uppercase letter in string\nPlease try again')
        elif lower==0:
            print('Error : There must atleast one lowercase letter in the password\nPlease try again')
        elif digit==0:
            print('Error : There must atleast one digit in the password\nPlease try again')
        elif len(password)<5 or len(password)>15:
            print('Error : The password lenght does\'nt match the constrains\nPlease try again')
        else:
            print('password generated successfully')
            with open("F:\GUVI\project.txt",'a') as f:
                d={}
                f.writelines((emailid+" "+password+'\n'))
                f.close()

elif user == 'login':
            file = open("F:\GUVI\project.txt", 'r')
            p=file.readlines()
            emailid = input('enter your emailid : ')
            for i in emailid:
                if i == '@' and emailid[emailid.index("@") + 1] == '.':
                    print("Error please don't  use \".\" after @\nPlease try again")
                    break
            new={}
            v= input('please enter your password if you have forget your password then enter forgot : ')
            if v=='forgot':
                for line in p:
                    if emailid in line:
                        x,z=line.split()
                        new[x]=z
                        print('your password is '+new[x])
            else:
                for line in p:
                    if line==(emailid+" "+v+'\n'):
                        print('you have successfully logged in ')
                        break


                else:
                    print('not a registered user please register or enter password is incorrect ')













