import sys

# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
def main():
    # read text from stdin
    text = sys.stdin.read()

    # Filter character given as an argument from the text
    remove_char = sys.argv[1]

    # Remove char from text
    adjusted_text = text.replace(remove_char, "")

    # Print the result to stdout
    sys.stdout.write(adjusted_text)
    
    # Print the total number of removed characters to stderr
    sys.stderr.write(str(text.count(remove_char)))


if __name__ == "__main__":
    main()
