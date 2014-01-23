# -*- coding: utf-8 -*-


class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person2(object):
    def __init__(self, first_name, last_name, birthday,
                 location, zipcode, country, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.location = location
        self.zipcode = zipcode
        self.country = country
        self.sex = sex
