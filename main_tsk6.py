# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі 
# Contact та UpdateContact.
import inspect
class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        
    def get_contact():
            pass
        
    def sent_message():
            pass
    
class UpdateContact(Contact):
      def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str, job: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        self.job = job

      def get_message(self):
            pass
# ============================================

first_contact = Contact("Jonson", "Jon", 16, 41241412124, "reprrr")
second_contact = UpdateContact("Jonson", "Petro", 16, 41241412124, "reprrr", "agagga")

def print_methods(item):
    for value in inspect.getmembers(item):
        print(value)
# ============================================

print("\n1- ", dir(Contact))
print("\n2- ", dir(UpdateContact))
print_methods(UpdateContact)