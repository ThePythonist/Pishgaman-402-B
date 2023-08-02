class Person:
    def __init__(self, fn, ln, age, job, ct):
        self.firstname = fn
        self.lastname = ln
        self.city = ct
        self.age = age
        self.job = job

    def talk(self):
        print(f"""
        Hello my name is {self.firstname} {self.lastname} and I am {self.age} years old
        and I live in {self.city} and I am a {self.job}.
        """)


student = Person("Ali", "Kamrani", 27, "Python Programmer", "Tabriz")
student.talk()
