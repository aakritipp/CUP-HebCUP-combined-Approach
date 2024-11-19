import csv
import os


def calculate_ncsm(old_code, new_code):
    # Calculate lengths of the code strings
    old_size = len(old_code)
    new_size = len(new_code)

    # Calculate NCSM
    ncsm = min(old_size, new_size) / max(old_size, new_size)

    return ncsm


if __name__ == "__main__":
    # Define input and output file paths
    input_csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'CSV-RAW-data', 'Java_train.csv')
    output_csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'CSV-Labeled-data', 'labeled_java_train.csv')

    # Read data from the input CSV file
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Modify data and write back to the output CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in rows:
            old_code = row[0] if row else ''
            new_code = row[1] if len(row) > 1 else ''

            ncsm = calculate_ncsm(old_code, new_code)
            label = "CUP" if ncsm > 0.89 else "hebCUP"

            row.append(label)
            row.append(ncsm)  # Append NCSM score to the row
            writer.writerow(row)

print("New labeled CSV file generated successfully!")
