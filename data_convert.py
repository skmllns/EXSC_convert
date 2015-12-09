import csv
import re

r_path = "single_line.csv"
w_path = "final_vs.csv"


new_header_elem = ['BIOL_108', 'BIOl 109', 'EXSC 110', 'EXSC 140', 'ACT English', 
                  'ACT Math', 'ACT Reading', 'ACT Science', 'ACT Comp', 'SAT Verbal', 
                  'SAT Math', 'SAT Comp']
                  
r_csv_file = open(r_path, 'rb')
w_csv_file = open(w_path, 'wb')

reader = csv.reader(r_csv_file)
writer = csv.writer(w_csv_file)

#skip header
reader.next()

for row in reader:
   for idx in range(len(new_header_elem)):
      writer.writerow([', '.join([str(elem) for elem in row[0:6]]), new_header_elem[idx], row[idx]])
              
r_csv_file.close()
w_csv_file.close()
  











