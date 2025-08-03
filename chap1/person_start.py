class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

    def lastName(self):
        return self.name.split()[-1]
    
    def firstName(self):
        return self.name.split()[0]
    
    def giveRaise(self, percent):
        self.pay *= (100.0 + percent)





if __name__ == '__main__':
    bob = Person('Bob Smith', 43, 40000, 'software')
    sue = Person('Sue Jones', 32, 15000, 'cam girl')
    #print(bob.name, sue.pay)
    
    #rint(bob.name.split()[-1])
    print(bob.lastName())
    print(sue.firstName())
    sue.giveRaise(.10)
    print(sue.pay)
        