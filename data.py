import pandas as pd

class obj:
    def __init__(self,email,name):
        self.email=email
        self.name=name
        
class Database:
    def __init__(self):
        self.data=pd.read_csv(r'C:\Users\anit4\OneDrive\Desktop\udemypy\SMTP\Automated Birthday Wisher\birthdays.csv')
    def get_data(self,month,day):
        output=[]
        for i in self.data.iterrows():
            if i[1]['month']==month and i[1]['day']==day:
                output.append(obj(i[1]['email'],i[1]['name']))
        return output


    