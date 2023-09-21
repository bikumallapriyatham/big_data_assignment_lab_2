import sys
bigram_counts = {}
if len(sys.argv) != 3:
    print("Usage: python bigram_count.py input_file.txt output_file.txt")
    sys.exit(1)
input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    with open(input_file, "r") as file:
        for line in file:
            words = line.strip().split()
            for i in range(len(words) - 1):
                bigram = f"{words[i]},{words[i+1]}"
                if bigram in bigram_counts:
                    bigram_counts[bigram] += 1
                else:
                    bigram_counts[bigram] = 1
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)
try:
    with open(output_file, "w") as output:
        for bigram, count in bigram_counts.items():
            output.write(f"{bigram}: {count}\n")
    print(f"Bigram count results saved to '{output_file}'.")
except IOError:
    print(f"Error: Unable to write to output file '{output_file}'.")
    sys.exit(1)
