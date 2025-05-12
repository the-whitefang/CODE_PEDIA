import sys
print('argument list', sys.argv)
first = int(sys.argv[1])
second = int(sys.argv[2])
print(f"Sum = {format(first + second)}")