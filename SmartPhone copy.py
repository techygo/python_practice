from Address import Address

class SmartPhone:
    def __init__(self):
        self.address_list = []

    def input_addr_data(self):
        self.name = input(" 이름을 입력하시오. : ")
        self.phone = input(" 전화번호를 입력하시오 : ")
        self.email = input(" 이메일을 입력하시오 : ")
        self.address = input(" 주소를 입력하시오. :")
        self.group = input(" 그룹(친구/가족)을 입력하시오. :")
        address = Address(self.name, self.phone, self.email, self.address, self.group)
        address.print_info()
        return address
        
    def add_addr(self, addr):
        self.address_list.append(addr)
        return 

    def print_all_addr(self):
        for addr in self.address_list:
            Address.print_info(addr)
        return

    def search_addr(self, name):
        for addr in self.address_list:
            if addr.name == name:
                Address.print_info(addr)
        return
        
    def delete_addr(self, name):
        for i, addr in enumerate(self.address_list):
            if addr.name == name:
                del self.address_list[i]
        return
        
    def edit_addr(self, name, new_addr):
        for i, addr in enumerate(self.address_list):
            if addr.name == name:
                addr.name = new_addr.name
                addr.phone = new_addr.phone
        return    
            

    