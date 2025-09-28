# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact,
# sent_message. Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, 
# job. Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою 
# атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.
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
    
class UpContact:
     pass
    
class UpdateContact(Contact, UpContact):
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

print("1: ", first_contact.__dict__)
print("2. ", Contact.__dict__)
print("3. ", Contact.__base__)
print("4. ", Contact.__bases__)
print("5: ", second_contact.__dict__)
print("6: ", UpdateContact.__dict__)
print("7: ", UpdateContact.__base__)
print("8: ", UpdateContact.__bases__)
