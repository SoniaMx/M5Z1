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