import sys
import re

line = sys.stdin.readline().strip()
if not re.match(r'^\d+$', line):
    print("Invalid input: first line must be an integer.")
    sys.exit(43)