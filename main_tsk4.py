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

print("1- ", isinstance(first_contact, Contact))
print("2- ", isinstance(second_contact, Contact))
print("3- ", isinstance(first_contact, UpdateContact))
print("4- ", isinstance(second_contact, UpdateContact))
print("5- ", issubclass(type(first_contact), Contact))
print("6- ", issubclass(first_contact.__class__, Contact))
print("7- ", issubclass(type(second_contact), Contact))
print("8- ", issubclass(type(first_contact), UpdateContact))
print("9- ", issubclass(type(second_contact), UpdateContact))