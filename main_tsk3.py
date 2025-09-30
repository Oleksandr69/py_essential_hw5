# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
#  Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
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
# ============================================

print("1- ", hasattr(first_contact, "surname"))
print("2- ", hasattr(first_contact, "supername"))
print("3- ", hasattr(second_contact, "job"))
delattr(second_contact, "job")
print("4- ", hasattr(second_contact, "job"))
setattr(second_contact, "my_job", "my_super_job")
print("5- ", hasattr(second_contact, "my_job"))
print("6- ", getattr(second_contact, "name"))
# hasattr(), getattr(), setattr(), delattr()