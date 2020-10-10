#Erick Jimenez
#PSID: 1463639
#Zylab 6.17 - Password Modifier

lab=input()
password=''
for x in lab:
    if(x=='i'):
        password+="!"
    elif(x=='a'):
        password+="@"
    elif(x=='m'):
        password+="M"
    elif(x=='B'):
        password+="8"
    elif(x=='o'):
        password+="."
    else:
        password+= x

password+="q*s"
print(password)