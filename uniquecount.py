import sys
word_counts = {}
if len(sys.argv) != 3:
    print("Usage: python wordcount.py input_file.txt output_file.txt")
    sys.exit(1)
input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    with open(input_file, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip('.,?!-";:')
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)
try:
    with open(output_file, "w") as output:
        for word, count in word_counts.items():
            output.write(f"{word}: {count}\n")
    print(f"Word count results saved to '{output_file}'.")
except IOError:
    print(f"Error: Unable to write to output file '{output_file}'.")
    sys.exit(1)
