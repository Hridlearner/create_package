
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
       # self.email = first+'.'+last+'@gmail.com'
    @property
    def email(self):
        return self.first + '.' + self.last+'@gmail.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name')
        self.first = None
        self.last = None


def main():
    emp1 = Employee('hrid', 'biswas')
    #emp1.first = 'yasemin'
    emp1.fullname = 'hrid biswas'


    print(f"first name ={emp1.first} Full name = {emp1.fullname} and Email = {emp1.email}")

    del emp1.fullname


if __name__=='__main__':
    main()