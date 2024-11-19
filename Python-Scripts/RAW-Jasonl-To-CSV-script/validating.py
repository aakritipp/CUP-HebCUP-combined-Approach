import json
import csv
import os

# Directory paths relative to the script's location
jsonl_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'Jasonl-RAW-data','HebCUP_clean_dataset','HebCUP_clean_dataset')
csv_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'CSV-RAW-data')

# Input and output file paths
jsonl_path = os.path.join(jsonl_dir, 'valid_clean.jsonl')
csv_path = os.path.join(csv_dir, 'Java_valid.csv')

# Open JSONL file for reading
with open(jsonl_path, 'r', encoding='utf-8') as jsonl_file:
    # Open CSV file for writing
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Source', 'Target', 'ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Read each line of the JSONL file
        for line in jsonl_file:
            # Load JSON data from the line
            data = json.loads(line)

            # Extract required fields
            id = data['sample_id']
            source = data['src_method']
            target = data['dst_method']

            # Write extracted data to CSV
            writer.writerow({'Source': source, 'Target': target, 'ID': id})

print("valid CSV file generated successfully!")
