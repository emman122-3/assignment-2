# Program Name: Assignment2.py
# Course: IT3883/Section w01
# Student Name: Emmanuel osime
# Assignment Number: 2
# Due Date: 02/18/2026
# Purpose:
# This program reads student data from a file, calculates the final average
# for each student based on six scores, and prints the results in descending
# order by average grade.
# Resources Used:
# Python documentation, course notes.

# Function to process student data
def calculate_averages(filename):
    students = []

    # Open and read the input file
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into parts
            parts = line.strip().split()

            # First element is the student's name
            name = parts[0]

            # Remaining elements are scores (convert to integers)
            scores = list(map(int, parts[1:]))

            # Calculate average
            average = sum(scores) / len(scores)

            # Store the result
            students.append((name, average))

    # Sort students by average in descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print the results
    print("Final Averages (Descending Order):")
    for name, avg in students:
        print(f"{name} {avg:.2f}")


# Main program
if __name__ == "__main__":
    input_file = "students.txt"
    calculate_averages(input_file)
