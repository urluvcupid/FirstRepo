# #ООП - объектно-ориентированное программирование
# # Наследование
#
# class Grandfather:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}\n"\
#                 f"Surname: {self.surname}\n"\
#                 f"Age: {self.age}\n"
#
#     def job(self):
#         return ("He is a doctor")
#
# grandfather = Grandfather(name="Adam",
#                           surname="Baker",
#                           age=58)
# print(grandfather)
# print(grandfather.job())
#
#
# class Father(Grandfather):
#     def __init__(self,name, surname, age, lastname):
#         super().__init__(name, surname, age)
#         self.lastname = lastname
#
#
#     def __str__(self):
#         return super(Father, self).__str__()\
#             +f"Lastname: {self.lastname}\n"
#
#     def job_father(self):
#         return ("He is a soccer player")
#
# father = Father (name="John",
#                  surname="Baker",
#                  age=33,
#                  lastname="Adamovich")
# print(father)
# print(father.job_father())
#
#
#
# class Son(Father):
#     def __init__(self, name, surname, age, lastname, reputation):
#         super(Son, self).__init__(name, surname, age, lastname)
#         self.reputation = reputation
#
#     def __str__(self):
#         return super(Son, self).__str__()\
#             + f"Reputation:{self.reputation}\n"
#
#     def job_son(self):
#             return ("He is a student")
#
# son = Son(name="Almaz",
#           surname="Adamov",
#           age=12,
#           lastname="Johnovich",
#           reputation="respected man")
#
# print(son)
# print(son.job_son())


class First_Phone:
    def __init__(self, creator, release, country):
        self.creator = creator
        self.release = release
        self.country = country
    def __str__(self):
        return f"Creator: {self.creator}\n"\
                f"Release: {self.release}\n"\
                f"Country: {self.country}\n"

    def job(self):
        return ("First opportunity to call from house")

first_phone = First_Phone(creator="Antonio Meucci",
                          release=1860,
                          country="USA")
print(first_phone)
print(first_phone.job())

class Portable_Phone(First_Phone):
    def __init__(self, creator, release, country, placement):
        super().__init__(creator, release, country)
        self.placement = placement

    def __str__(self):
        return super(Portable_Phone, self).__str__()\
            +f"Placement: {self.placement}\n"

    def job_portable(self):
        return ("Can be anywhere")

portable_phone = Portable_Phone (creator= "Martin Cooper",
                                release=1973,
                                country="USA",
                                placement="Everywhere")
print(portable_phone)
print(portable_phone.job_portable())

class Iphone(Portable_Phone):
    def __init__(self,creator,release,country,placement,price):
        super().__init__(creator,release,country,placement)
        self.price = price

    def __str__(self):
        return super(Iphone, self).__str__()\
            +f"Price: {self.price}\n"

    def job_iphone(self):
        return ("Can fit in pocket")

iphone = Iphone (creator="Steve Jobs",
                 release=2007,
                 country="USA",
                 placement="Pocket",
                 price="599$")
print(iphone)
print(iphone.job_iphone())


