
class Address:
    def __init__(self, name, phone, email, address, group):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__group = group

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address
    
    @property
    def group(self):
        return self.__group

    def print_info(self):
        print(f" 이름 : {self.name}")
        print(f" 전화번호 : {self.phone}")
        print(f" 이메일 : {self.email}")
        print(f" 주소 : {self.address}")
        print(f" 그룹(친구/가족) : {self.group}")

