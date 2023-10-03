#!/usr/bin/env python3
# Created by: souleye keita
# Created on: oct. 3, 2023
# This program asks the user for the length and
# width of the rectangle in mm. It then
# calculates and displays the area and
# perimeter.
import math


def main():
    # get length and width
    print("Today we will calculate the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # calculating area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # shows area and perimeter
    print("")
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
