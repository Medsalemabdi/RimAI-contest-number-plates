
#Converting the text data obtained from easy ocr to csv format 
import csv

input_log_file = 'log_demo_result (3).txt'
output_csv_file = 'log_demo_result (3).csv'

# Function to manually parse each line assuming fixed-width columns
def parse_line(line):
    # Assuming the columns are at fixed positions based on your example
    image_path = line[:25].strip()          # First 25 characters
    predicted_labels = line[26:49].strip()  # Next 23 characters
    confidence_score = line[50:].strip()    # The rest of the line
    
    return [image_path, predicted_labels, confidence_score]

# Read the log file and write to a CSV file
with open(input_log_file, 'r') as infile, open(output_csv_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Write the header
    writer.writerow(['image_path', 'predicted_labels', 'confidence_score'])

    # Process each line in the log file
    for line in infile:
        parsed_row = parse_line(line)
        writer.writerow(parsed_row)

print("Log file has been converted to CSV.")
