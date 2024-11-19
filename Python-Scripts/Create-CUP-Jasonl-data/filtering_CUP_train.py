import csv
import json
import os

def read_jsonl_file(jsonl_file):
    """Reads data from a JSONL file and returns it as a list of dictionaries."""
    data = []
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def write_jsonl_file(data, filename):
    """Writes data to a JSONL file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file)
            file.write('\n')

if __name__ == "__main__":
    # Define file paths
    csv_file = os.path.join(os.path.dirname(__file__), '..', '..','Data', 'CSV-Labeled-data', 'labeled_java_train.csv')
    jsonl_file = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'Jasonl-RAW-data','HebCUP_clean_dataset','HebCUP_clean_dataset','train_clean.jsonl')
    output_jsonl_file = os.path.join(os.path.dirname(__file__), '..', '..','Data', 'CUP-Jasonl-data', 'filtered_data_trainCUP.jsonl')

    # Read the CSV file and identify rows labeled "CUP"
    cup_rows = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[3] == "CUP":  # Assuming the label is in the fourth column
                cup_rows.append(int(row[2]))  # Convert ID to integer

    # Read JSONL file and filter data based on cup_rows
    filtered_data = []
    jsonl_data = read_jsonl_file(jsonl_file)
    jsonl_ids = [item['sample_id'] for item in jsonl_data]

    for item in jsonl_data:
        if int(item['sample_id']) in cup_rows:  # Convert ID to integer for comparison
            filtered_data.append(item)

    # Write filtered data to a new JSONL file
    write_jsonl_file(filtered_data, output_jsonl_file)

    print("Filtered data saved successfully to:", output_jsonl_file)
