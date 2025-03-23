import csv

def append_new_words_to_csv(input_file, output_file):
    # Initialize variables
    new_words = []

    # Read the words.txt file
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Process the lines to extract French words and their definitions
    for i in range(0, len(lines), 3):  # Step by 3 because of the empty line
        french_word = lines[i].strip()  # French word on line i
        definition = lines[i + 2].strip() if i + 2 < len(lines) else ""  # Definition on line i+2
        if french_word and definition:  # Ensure both are non-empty
            new_words.append((french_word, definition))

    # Append new words to the existing CSV file
    with open(output_file, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for word, definition in new_words:
            writer.writerow([word, definition])

    print(f"Appended {len(new_words)} new words to '{output_file}' successfully!")

# Example usage
input_file = "words.txt"  # Replace with your file path
output_file = "words.csv"
append_new_words_to_csv(input_file, output_file)
