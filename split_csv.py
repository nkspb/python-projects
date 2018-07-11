"""
Split a csv file into multiple files with a specified number of rows
By Nikolay Komolov
github.com/nkspb
"""

import sys, os, argparse, csv

# Grab cli arguments
parser = argparse.ArgumentParser(
    description="CSV split tool.",
    epilog="""
        Split an input csv file (-i) into multiple output files (-o)
        with a specified number of rows (-r).
    """
)
parser.add_argument("-i", dest="input_file", help="An input file to split", required=True)
parser.add_argument("-o", dest="output_file", help="A base name for files after splitting", required=True)
parser.add_argument("-r", dest="row_limit", help="Number of rows limit after which perform splitting", required=True)
args = parser.parse_args()

# Calculate number of rows minus the header
def count_rows(input_file):
    with open(input_file) as f:
        # Itterate through rows to get a final value of index
        # This way we can find the number of rows
        for index, value in enumerate(f):
            pass
    # Return number of rows in a file, not including the header
    return index

# Check if file exists
def check_arguments():
    if not os.path.isfile(args.input_file):
        print("The {} file doesn't exists".format(args.input_file))
        exit()

    # Check if number of rows is less than\equals rows limit
    if count_rows(args.input_file) <= int(args.row_limit):
        print("The number of rows in {} is less than\equal to row_limit ({})".format(args.input_file, args.row_limit))
        exit()

# Check arguments provided to the script
check_arguments()

def split_csv(input_file, row_limit):
    # This list contains rows, where each row is a list
    rows_list = []
    # This list will contain all chunks
    chunks = []

    with open(input_file, "r") as f:
        csv_reader = csv.reader(f)
        # Save the header to a variable, cause we need it to append to output files
        header = next(csv_reader)
        # Construct a list of lists with rows from the csv file
        for row in csv_reader:
            rows_list.append(row)

        # Set the starting row
        row_count = 0
        chunk = []

        for i, row in enumerate(rows_list):
            # We need to count to the row limit
            row_count += 1
            # Add header if this is the first row of a chunk
            if row_count == 1:
                chunk.append(header)
            if row_count <= int(row_limit):
                # add to the chunk until row limit is reached
                chunk.append(row)
                # If this was the last row, append final chunk to chunks
                if i == len(rows_list) - 1:
                   chunks.append(chunk) 
            else:
                # Start counting rows from the beginning
                row_count = 1
                # Append the resulting chunk to chunks  
                chunks.append(chunk)
                # As we've reached the row_limit, we start building a new chunk
                # Clear the chunk
                chunk = []
                chunk.append(header)
                chunk.append(row)
                # If this was the last row, append final chunk to chunks
                if i == len(rows_list) - 1:
                   chunks.append(chunk)
        
        return chunks

chunks = split_csv(args.input_file, args.row_limit)

# Save chunks to output files
def save_chunks(output_file, chunks):
    # Go through each chunk in chunks
    for i, chunk in enumerate(chunks):
    # Save each to a separate file in the output directory
        
        # Split the extension and add it back after modifying the name
        new_file_name = os.path.splitext(output_file)[0] + "_" + str(i) + ".csv"
        with open(new_file_name, "w", newline="\n") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(chunk) 
            print("Saved as {}. There are {} rows in it.".format(new_file_name, len(chunk) - 1))

save_chunks(args.output_file, chunks)

