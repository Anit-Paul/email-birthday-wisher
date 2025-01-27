import datetime as dt
from data import *
import random
import os
import smtplib

class Birthday:
    def __init__(self):
        self.file=Database()
        self.path=r'' #the folder of the letters
        self.sender='' #sender email
        self.password='' #app password for sender email
    
    def __send_email(self,content,name,receiver):
        letter=content.replace('[NAME]',name)
        try:
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                try:
                    connection.starttls()
                    connection.login(user=self.sender,password=self.password)
                except Exception as e:
                    print(e)
                    return False
                else:
                    try:
                        connection.sendmail(from_addr=self.sender, to_addrs=receiver, msg=f"Birthday Wish\n\n{letter}")
                    except Exception as e:
                        print(e)
                        return False
                    else:
                        return True
        except Exception as e:
            print(e)
            return False
                
        
        
    def __get_letter(self,letter_choice):
        letter_path=os.path.join(self.path,letter_choice)
        try:
            with open(letter_path,'r') as letter:
                content=letter.read()
        except Exception as e:
            return f'Something went wrong! {e}'
        else:
            return content
        
    def wish(self):
        date=dt.datetime.now()
        data=self.file.get_data(date.month,date.day)
        letter=random.randint(1,3)
        for i in data:
            letter_choice=f'letter_{letter}.txt'
            content=self.__get_letter(letter_choice)
            if self.__send_email(content,i.name,i.email):
                print(f'letter sended to {i.name} successfully!')
            else:
                print(f'something went wrong for {i.name}')

def main():
    Birthday().wish()

if __name__=='__main__':
    main()



