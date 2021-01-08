#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program calculates the surface area of a sphere

import math


def sphere_surface(radius):
    # This program calculates the surface area of a sphere

    # process
    surface_area = math.pi * 4 * (radius * radius)

    return surface_area


def main():
    # this function receives input
    print("This program calculates the surface area of a sphere.")
    print("")

    # input
    while True:
        try:
            radius_input = input("Enter the radius (cm): ")
            radius_int = int(radius_input)
            print("")

            if radius_int > 0:
                # call function
                sphere = sphere_surface(radius_int)

                surface_rounded = '{0:.4g}'.format(sphere)

                print("A sphere with a radius of {0} cm has a surface"
                      " area of {1} cm²."
                      .format(radius_int, surface_rounded))

                break
            else:
                # output
                print("Enter a positive integer for both values, try again.")
                print("")
        except Exception:
            # output
            print("Enter a number for both values, try again.")


if __name__ == "__main__":
    main()
