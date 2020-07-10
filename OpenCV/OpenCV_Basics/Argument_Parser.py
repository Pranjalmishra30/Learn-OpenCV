# Type in python3 Argument_Parser.py -h for more info
import math
import argparse

def volume_cone (radius , height):
    v = (1/3)* math.pi * (radius**2)* height
    return v

parser = argparse.ArgumentParser(description="Calculate volume of a cone")
parser.add_argument('-r','--Radius',type=float,help='Radius of cone') # These are now optional arguments
parser.add_argument('-H','--Height',type=float,help='Height of cone')
args  = parser.parse_args()

print(volume_cone(args.Radius,args.Height))
