# Imports
import numpy as np
import argparse


def calculate_cylinder_volume(radius, height):
    volume = np.pi * radius**2 * height
    return volume


parser = argparse.ArgumentParser(description="Calculate volume of a cylinder")
parser.add_argument('-r', '--radius', type=int, metavar="", required=True, help='Radius of a cylinder')
parser.add_argument('-H', '--height', type=int, metavar="", required=True, help='Height of a cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

if __name__ == "__main__":
    volume = calculate_cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"The volume of a cylinder with radius {args.radius} and {args.height} is {volume}")
    else:
        print(f'Volume of cylinder is {volume}')