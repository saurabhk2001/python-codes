#python has encapsulation
#1)public- is use in directly in all classes and methods
#2)private- is only use in class won class
#3)protected-are only use in derive class,i.e class are inheritade

#public
class person:
    def __init__(self):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)



name="saurabh"
age=22
x=person()
x.display()
print(x.name)
print(x.age)


# protected

class person:
    def __init__(self):
        self._name=name
        self._age=age

    def display(self):
        print(f"the name is {self._name} and age is{self._age}")


class person2(person):
    def __init__(self):
     person. __init__(self)
     self.no=no

    def show(self):
        print(self._name,self._age,self.no)


name="saurabh"
age=22
no=2345345
x=person2()
x.display()

print(x._name)


#private
class person:
    def __init__(self):
        self.__name=name
        self.__age=age

    def display(self):
        print(self.__name,self.__age)

class person2(person):
    def __init__(self):
        person.__init__(self)
        self.no=no

    def show(self):
        print(self._person__name,self._person__age,self.no)


name="saurabh"
age=22
no=2234567
x=person2()
x.show()
print(x._person__name)  #not good practice for industri keep it private'''

              
