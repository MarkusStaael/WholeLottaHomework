import sys
import re

def main():
    try:
        # Read and validate n
        n_line = sys.stdin.readline()
        if not n_line or not n_line.strip().isdigit():
            sys.exit(43)
        n = int(n_line.strip())
        if not (1 <= n <= 100000):
            sys.exit(43)

        # Compile regex for a single line: "a op b" with 0 <= a,b <= 99
        pattern = re.compile(r'^(0|[1-9]\d?) ([+-]) (0|[1-9]\d?)$')

        # Validate exactly n lines
        for i in range(n):
            line = sys.stdin.readline()
            if not line:
                sys.exit(43)
            line = line.rstrip('\n')  # remove trailing newline
            if not pattern.fullmatch(line):
                sys.exit(43)

        # Check for extra content after the last line
        extra = sys.stdin.read().strip()
        if extra != '':
            sys.exit(43)

        sys.exit(42)  # all checks passed
    except Exception:
        sys.exit(43)

if __name__ == "__main__":
    main()