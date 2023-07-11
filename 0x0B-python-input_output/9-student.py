#!/usr/bin/python3
"""
This module contains a Student class that defines a student with
first_name, last_name, and age attributes, and a method to retrieve
a dictionary representation of the student instance.
"""


class Student:
    """
    Student class with public instance attributes and a method to
    retrieve a dictionary representation of the student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with given first_name, last_name, age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        return self.__dict__


if __name__ == "__main__":
    Student = __import__('9-student').Student

    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
