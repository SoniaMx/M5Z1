#podpunkt 1
class BaseContact:
    def __init__(self, name, surname, private_phone, email):
        self.name = name
        self.surname = surname
        self.private_phone = private_phone
        self.email = email

class BusinessContact(BaseContact):
    def __init__(self, job_position, company_name, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_position = job_position
        self.company_name = company_name
        self.work_phone = work_phone
#podpunkt 2
    def private_contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.name} {self.surname}"
    def business_contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}"
    
    @property
    def name_length(self):
        return len(self.name)
    @property
    def surname_length(self):
        return len(self.surname)
    
first_person = BusinessContact(name = "Wanda", surname = "Janik", private_phone = "+48 987345765", email = "ajhjjb@.pl", job_position = "Risk Manager", company_name = "KPMG", work_phone = "+48 123456789")
second_person = BusinessContact(name = "Jadzia", surname = "Kowalik", private_phone = "+48 865234909", email = "sjsaa@.pl", job_position = "HR Specialist", company_name = "IBM", work_phone = "+48 456321876")
third_person = BusinessContact(name = "Andrea", surname = "Bilik", private_phone = "+48 555888999", email = "bcvsgd@.pl", job_position = "Payable Supervisor", company_name = "EY", work_phone = "+48 333555444")
fourth_person = BusinessContact(name = "Nela", surname = "Ufnał", private_phone = "+48 225768908", email = "ijwna@.pl", job_position = "Agile Manager", company_name = "Daimler Benz AG", work_phone = "+48 777666222")
fifth_person = BusinessContact(name = "Klara", surname = "Czarnik", private_phone = "+48 111999000", email = "hsgwy@.pl", job_position = "Fashion Buyer", company_name = "Luxotica", work_phone = "+48 333000444")

print(first_person.private_contact())
print(second_person.private_contact())
print(third_person.private_contact())
print(fourth_person.private_contact())
print(fifth_person.private_contact())

print(first_person.business_contact())
print(second_person.business_contact())
print(third_person.business_contact())
print(fourth_person.business_contact())
print(fifth_person.business_contact())
#podpunkt 3
print(f"Ilość liter imienia {first_person.name}: {first_person.name_length}, ilość liter nazwiska {first_person.surname}: {first_person.surname_length}")
print(f"Ilość liter imienia {second_person.name}: {second_person.name_length}, ilość liter nazwiska {second_person.surname}: {second_person.surname_length}")
print(f"Ilość liter imienia {third_person.name}: {third_person.name_length}, ilość liter nazwiska {third_person.surname}: {third_person.surname_length}")
print(f"Ilość liter imienia {fourth_person.name}: {fourth_person.name_length}, ilość liter nazwiska {fourth_person.surname}: {fourth_person.surname_length}")
print(f"Ilość liter imienia {fifth_person.name}: {fifth_person.name_length}, ilość liter nazwiska {fifth_person.surname}: {fifth_person.surname_length}")