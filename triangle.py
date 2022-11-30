#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program calculates area of a triangle


import random


def area_of_triangle(int_base, int_height):
    # calculate area

    # process
    area = int_base * int_height / 2

    # output
    print("The area of the triangle is: {0}cm².".format(area))


def main():
    # input
    string_base = input("Enter the base of the triangle (cm): ")
    string_height = input("Enter the height of the triangle (cm): ")

    try:
        int_base = int(string_base)
        int_height = int(string_height)
        # call functions
        area_of_triangle(int_base, int_height)
    except ValueError:
        print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
