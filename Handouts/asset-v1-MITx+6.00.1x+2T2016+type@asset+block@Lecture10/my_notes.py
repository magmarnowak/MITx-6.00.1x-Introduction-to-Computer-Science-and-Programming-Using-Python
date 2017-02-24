import datetime
class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        """set self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
             return self.name < other.name
        return self.name < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name


m1 = Person('Mark Zuckerberg')
m1.setBirthday(5,14,84)
m2 = Person('Drew Houston')
m2.setBirthday(3,4,83)
m3 = Person('Bill Gates')
m3.setBirthday(10,28,55)
m4 = Person('Travis Kalanik')
m5 = Person('Steve Wozniak')

personList = [m1, m2, m3, m4, m5]

print(personList.sort())
