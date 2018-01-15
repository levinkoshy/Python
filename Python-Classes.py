class Dog():
    name ="Jon"
    colour="brown"

>>> Dog
<class __main__.Dog at 0x0000000005556B88>
>>> Dog() #instance
<__main__.Dog instance at 0x0000000005581C48>

#creating objects/instances of the class

//Class - example Human beings ; Object: People
//Objects can have common features of their class; as well as different features

instance = Dog()
obj = Dog()
object = Dog()

>>> obj.name
'Jon'
>>> obj.name="Walter"
>>> obj.name
'Walter'

class Dog():
    name ="Jon"
    colour="brown"
    def get_color(self):
        return self.colour 

obj = Dog()

# implies that obj is the self now; obj = self

>>> obj.get_color()
'brown'

obj.colour = "white"
obj.get_color()
//'white'

class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise


dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


//Inheritence
//Animal :parent class. Child class Dog inherits the attributes from parent class.

class Dog(Animal):
    name = 'Jon'
    size = "small"
    color = "black"
    age = 19


jon = Dog()
jon.color = 'white'
jon.name = 'Jon Snow'


//KeyWord Arguments: to make the arguments "Not Required"; we can define it in the function call

//@property makes a function to be called like obj.get_color instead of calling obj.get_color()


-----------------------------------------------------------------------------------------------------
import datetime
class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
    def add_user(self,name,amount,email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
            "name" : name,
            "amount" : amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today = today)
        detail["date"] = date_text
        if email is not None: #email != None
            detail["email"] = email	
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name = name,
                    date = date,
                    total = amount
                )    
                self.messages.append(new_msg)
            return self.messages
        return []


obj = MessageUser()
obj.add_user("Justin", 123.32)
obj.add_user("joHn", 94.23)
obj.add_user("Levin", 94.23, email="lkoshy@iastate.edu")
obj.add_user("Emily", 94.23)
obj.get_details()
obj.make_messages()
//{'date': '1/14/2018', 'amount': '123.32', 'name': 'Justin'}, {'date': '1/14/2018', 'amount': '94.23', 'name': 'John'}]


//We can import the MessageUser() class in a different program
// from 'file_name' import MessageUser()


//if you create a python file in a folder; that folder will be considered as a python module
//if the folder "Msg" contains a file "messages.py"
//from Msg.messages import MessageUser

