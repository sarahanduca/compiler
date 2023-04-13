import sys
from analyzers.parser_build import analyze_code

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "test_files/test_input.txt"

    code_input = open(filename, "r")
    code_file = code_input.read()

    analyze_code(code_file)
