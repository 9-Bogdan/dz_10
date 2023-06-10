from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
        if phone:
            self.phones = []
            self.phones.append(phone)

    def remove_phone(self):
        for num in self.phones:
            if num.value == self.phone:
                self.phones.remove(num)

    def edit_phone(self, old_number, new_number):
        for num in self.phones:
            if num.value == old_number:
                num.value = new_number


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
