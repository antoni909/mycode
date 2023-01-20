#!/usr/bin/python3
import csv

def main():
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                print('Column names are {}'.format(", ".join(row)))

                line_count += 1
            with open('regularbirthday.csv', mode='a') as reg_bday:
                reg_bday.write('\t{} aka {} was born in {}.'.format(row["name"],row["birthday month"]))
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))

if __name__ == "__main__":
    main()

