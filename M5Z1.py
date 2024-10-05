#podpunkt 1
class BaseContact:
    def __init__(self, name, surname, private_phone, email)
        self.name = name
        self.surname = surname
        self.private_phone = private_phone
        self.email = email

class BusinessContact(BaseContact):
    def __init__(self, job_position, company_name, work_phone, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.job_position = job_position
        self.company_name = company_name
        self.work_phone = work_phone
#podpunkt 2
    def private_contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.name} {self.surname}"
    def business_contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}"
    
first_person = BaseContact(name = "Wanda", surname = "Janik", private_phone = "+48 987345765", email = "ajhjjb@.pl", job_position = "Risk Manager", company_name = "KPMG", work_phone = "+48 123456789")
second_person = BaseContact(name = "Jadzia", surname = "Kowalik", private_phone = "+48 865234909", email = "sjsaa@.pl", job_position = "HR Specialist", company_name = "IBM", work_phone = "+48 456321876")
third_person = BaseContact(name = "Andrea", surname = "Bilik", private_phone = "+48 555888999", email = "bcvsgd@.pl", job_position = "Payable Supervisor", company_name = "EY", work_phone = "+48 333555444")
fourth_person = BaseContact(name = "Nela", surname = "Ufnał", private_phone = "+48 225768908", email = "ijwna@.pl", jo_position = "Agile Manager", company_name = "Daimler Benz AG", work_phone = "+48 777666222")
fifth_person = BaseContact(name = "Klara", surname = "Czarnik", private_phone = "+48 111999000", email = "hsgwy@.pl", job_position = "Fashion Buyer", company_name = "Luxotica", work_phone = "+48 333000444")