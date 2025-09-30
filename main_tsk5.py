# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у
# класах Contact та UpdateContact та їх екземплярах. Видаліть атрибут job, і знову
# надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.
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
    
    def __str__(self):
         return f"{self.surname}, {self.name}, {self.age}, {self.mob_phone}, {self.email}"
    
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

print("\n1: ", first_contact.__dict__)
print("2. ", Contact.__dict__)
print("3: ", second_contact.__dict__)
print("4: ", UpdateContact.__dict__)
# ============================================

delattr(second_contact, "job")
# delattr(UpdateContact, "job")
print("5: ", second_contact.__dict__)
print("6: ", first_contact)