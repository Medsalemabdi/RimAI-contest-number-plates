#converting predictions to the submission template

import csv
import string

# Input and output file paths
input_log_file = 'log_demo_result (3).csv'
submission_template_file = 'submission_template.csv'
output_submission_file = 'submission (3).csv'

# Columns include digits 0-9 and letters A-Z
columns = ['X' + str(i) for i in range(10)] + list(string.ascii_uppercase)

# Function to create a one-hot encoded row for a character
def create_one_hot_row(char):
    row = ['0'] * len(columns)  # Initialize with zeros
    if char.isdigit():
        index = columns.index('X' + char)
    else:
        index = columns.index(char.upper())
    row[index] = '1'
    return row

# Process the log file and fill the submission template
with open(input_log_file, 'r') as infile, \
     open(submission_template_file, 'r') as templatefile, \
     open(output_submission_file, 'w', newline='') as outfile:
    
    reader = csv.DictReader(infile, delimiter=',')
    template_reader = csv.DictReader(templatefile)
    writer = csv.DictWriter(outfile, fieldnames=template_reader.fieldnames)
    
    writer.writeheader()  # Write the header to the output file
    
    for row in reader:
        image_path = row['image_path'].strip()
        predicted_labels = row['predicted_labels'].strip()
        
        for i, char in enumerate(predicted_labels):
            one_hot_row = create_one_hot_row(char)
            submission_id = f"{image_path.split('.')[0]}_{i + 1}"
            
            # Create the row for the submission file
            submission_row = {'id': submission_id}
            submission_row.update(dict(zip(columns, one_hot_row)))
            writer.writerow(submission_row)

print("Submission file has been created.")
