#!/usr/bin/env python3

# Created by: Tamer Zreg
# Created on: Sep 2022
# This program shows assingment statements


def main():
    number_of_students = 2
    width = 12.5
    length = 5.0
    some_words1 = "Hello"
    some_words2 = "World!"

    number_of_students = number_of_students**5
    area_of_rectangle = length * width
    hello_world = some_words1 + ", " + some_words2

    print("The number of students is: " + str(number_of_students))
    print("The area of a rectangle is: " + str(area_of_rectangle) + " cm²")
    print(hello_world)


if __name__ == "__main__":
    main()
