#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program calculates area and perimeter of triangle


def calculate_area(base_of_triangle: int, height_of_triangle: int) -> None:
    # calculate area

    # process
    area = (base_of_triangle * height_of_triangle) / 2

    # output
    print("The area of the triangle is {0} cm².".format(area))


def calculate_perimeter(
    base_of_triangle: int, side2_of_triangle: int, side3_of_triangle: int
) -> None:
    # calculate perimeter

    # process
    perimeter = base_of_triangle + side2_of_triangle + side3_of_triangle

    # output
    print("The perimeter of the triangle is {0} cm.".format(perimeter))


def main():
    # this function gets length and width

    # input
    base_of_triangle = int(input("Enter the base of the triangle (cm): "))
    height_of_triangle = int(input("Enter the height of the triangle (cm): "))
    side2_of_triangle = int(input("Enter the second side of the triangle (cm): "))
    side3_of_triangle = int(input("Enter the third side of the triangle (cm): "))
    print("")

    # call functions
    calculate_area(base_of_triangle, height_of_triangle)
    calculate_perimeter(base_of_triangle, side2_of_triangle, side3_of_triangle)


if __name__ == "__main__":
    main()
