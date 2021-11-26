#SPB( SECRET PHONE BOOK )
import pickle
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#pin manager

def sent_mail(b_id,b_file):
    mail_content='''There was an intruder trying to access your phonebook.
    Your data on that device is deleted.A backup copy of your data is here.
    Thank You'''
    sender_address='vedantyadav03@gmail.com'
    sender_pass='293@Story'
    receiver_address=b_id
    message=MIMEMultipart()
    message['From']=sender_address
    message['TO']=receiver_address
    message['Subject']='Intruder on your Secret phonebook'
    message.attach(MIMEText(mail_content,'plain'))
    attach_file_name=b_file
    attach_file=open(attach_file_name,'rb')
    payload=MIMEBase('application','ovtate-strem')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition','attachment',fiename=attach_file_name)
    message.attach(payload)
    session=smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()
    session.login(sender_address,sender_pass)
    text=message.as_string()
    session.sendmail(sender_address,receiver_address,text)
    session.quit()
def pinread():
    with open('pin.dat','rb') as pinfile:
        rec=pickle.load(pinfile)
        global pin
        global b_id
        pin=rec[0]
        b_id=rec[1]
try:
    pinread()
except FileNotFoundError:
    with open('pin.dat','wb') as pinfile:
        pn=input("set a password for phonebook!!! :  ")
        print('''Enter a backup email id of yours.
                This id will be used to send you your contact list and
                All the data on this system will be erased.
                This will happen if you enter wrong password in continous three attempts''',end=' ')
        backupid=input(":---  ")
        pickle.dump([pn,backupid],pinfile)
        print("password set succesfully")
    pinread()
def backup_func(cflt):
        with open(cflt,'rb') as cflr:
            data=pickle.load(cflr)
            with open('backup.txt','wb') as bk_file:
                pickle.dump(data,bk_file)
def conread():
    spb=open('contact.dat','rb')
    phonebook=pickle.load(spb)
    spb.close()
try:
    conread()
except FileNotFoundError:
    spb=open('contact.dat','wb')
    myname=input("Enter your name :----  ")
    mynum=input("Enter your number :---  ")
    hp=[]
    hp=[[myname,mynum]]
    pickle.dump(hp,spb)
    spb.close()
    conread()
for fff in range(0,3):
    pinin=input("Enter password :--  ")
    if pinin==pin:
        print("welcome user")
        break
    else:
        if fff==2:
            try:
                print("ALL TRIALS EXHAUSTED!!! INTRUDER SPOTTED")
                backup_func('contact.dat')
                sent_mail(b_id,'backup.txt')
                print("The entire directory has been mailed to registered Email id")
                print("Your data had been cleared from this device")
                os.remove('contact.dat')
                os.remove('pin.dat')
                os.remove('backup.txt')
                quit()
            except Exception as e:
                print("ALL TRIALS EXHAUSTED!!! INTRUDER SPOTTED")
                print("No internet connection,Backup can not be created")
                print("Deleting all the data from device........")
                print("Your data had been cleared from this device")
                quit()
        else:
            continue
def newcon(phonebook):              #(entering records into the phone book)
    while True:
        Name=input("ENTER THE NAME : ")
        Number=int(input("ENTER THE NUMBER : "))
        lat=[Name,Number]
        phonebook.append(lat)
        ch = input("Want to enter new record, Press y or Y :--  ")
        if ch not in ['y','Y']:
            break
    return phonebook
print('''Choose the function you want to operate :--
        1.To view all the contacts
        2.To view a specific contact
        3.To add new contact
        4.To update existing contact info
        5.To change password''')
opt=int(input("Enter the option number :--   "))
if opt==3:
    with open('contact.dat','rb') as cfle:
        global pb
        phonebook=pickle.load(cfle)
        pb=newcon(phonebook)
    spf=open('contact.dat','wb')
    pickle.dump(pb, spf)
    spf.close()
elif opt==5:
    if pin==input("please re-enter your password"):
        pinfiles=open('pin.dat','wb')
        newpin=input("Enter new password")
        pickle.dump([newpin,b_id],pinfiles)
        print("Password change successfully")
        pinfiles.close()
elif opt==4:
    cfls=open('contact.dat','rb')
    phonebook=pickle.load(cfls)
    choi=int(input("press 1 to search by name or press 2 to search by number"))
    if choi==1:
        searchname=input("Enter the name of contact you want to update")
        for I in phonebook:
            if I[0]==searchname:
                I[1]=int(input("Enter the new number of "+I[0]+"  :-- "))
    elif choi==2:
        searchnum=input("Enter the number of contact you want to update")
        for I in phonebook:
            if I[1]==searchnum:
                newname=input("Enter new name for this number "+str(I[1])+"  :-- ")
                I[0]=newname
    else:
            print("Invalid Choice")
    cfls=open('contact.dat','wb')
    pickle.dump(phonebook,cfls)
    cfls.close()
elif opt==2:
    cfls=open('contact.dat','rb')
    phonebook=pickle.load(cfls)
    chooi = int(input("press 1 to search by name or press 2 to search by number"))
    if chooi==1:
        nma=input("Enter the name :---  ")
        for IJ in phonebook:
            if IJ[0]==nma:
                temp20,temp21=IJ[0],str(IJ[1])
                print("Name = " + temp20)
                print("Number = " + temp21)
    elif chooi==2:
        nmu = input("Enter the number :---  ")
        for IJ in phonebook:
            if IJ[1] == nmu:
                temp20,temp21=IJ[0],str(IJ[1])
                print("Name = "+temp20)
                print("Number = "+temp21)
    cfls.close()
elif opt==1:
    spg=open('contact.dat','rb')
    xxcc=pickle.load(spg)
    for temp in xxcc:
        print(temp)
else:
    print("Option is incorrect")

vf=input("press any key to quit")
mn="qwertyuiopasdfghjklzxcvbnm,./';[]1234567890-==-!@#$%^&*()_+{:']}'<>?|"
if vf in mn:
    print("thank you for using it")


                
            


