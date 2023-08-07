# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# a = A()
# b = B()
# b.say_hello()


class Father:
    def __init__(self, fname, address, job):
        self.familyname = fname
        self.address = address
        self.job = job

    def say_hello(self):
        print("Hello")


class Child(Father):
    def __init__(self, fname, address, uni, job):
        super().__init__(fname, address, job)
        self.uni = uni

    def say_goodbye(self):
        print("Goodbye")


# pedar = Father("Ahmadi", "Ekbatan", "Teacher")
farzand = Child("Ahmadi", "Ekbatan", "Sharif", "Engineer")
print(farzand.address)
farzand.say_goodbye()
