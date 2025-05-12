import argparse
parser = argparse.ArgumentParser(description="Greet someone with name and age.")
parser.add_argument("name", help="Abhilash")
parser.add_argument("age",type=int, help="23")

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old.")
