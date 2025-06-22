import argparse

def ctof(n):
    result=(n*(9/5))+32
    return(result)

def ftoc(n):
    result=(n-32)*(5/9)
    return(result)

parser=argparse.ArgumentParser(description="converting temperatures")

group=parser.add_mutually_exclusive_group(required=True)

group.add_argument('-c',type=float,help='Celsius to fahrenheit')
group.add_argument('-f',type=float,help='Farenheit to celsius')

args=parser.parse_args()

if args.c is not None:
    x=ctof(args.c)
    print(f"Celsius {args.c} to fahrenheit {x}")
elif args.f is not None:
    x=ftoc(args.f)
    print(f"Fahrenheit {args.f} to Celsius {x}")
