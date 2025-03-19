import os
import csv

def write_csv(email,url,status):

    csv_file = "output.csv"
    write_header = not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Email","url","Status"])   
        writer.writerow([email,url,status]) 

        print(f"Data saved to {csv_file}")
    