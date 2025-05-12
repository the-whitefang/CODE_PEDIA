import argparse
parser = argparse.ArgumentParser(description="sample argument")
parser.add_argument("user")
args = parser.parse_args()
if args.user == "Admin":
    print("Hello Admin")
else:
    print("Hello Guest")