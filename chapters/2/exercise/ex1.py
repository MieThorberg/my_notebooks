import argparse
import csv
import platform

# prints content of a csv file to the console
def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        print(header_row)
        for row in reader:
            print(str(row))


# takes a list of tuples of strings
# and write each element to a new line in file
def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None

    with open(output_file, 'w', newline=newline) as o:
        output_writer = csv.writer(o)

        for el in lst:
            output_writer.writerow(el)


# takes a random number of strings
# and write each element to a new line in file
def write_elements_to_file(output_file, *elements):
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None

    with open(output_file, 'w', newline=newline) as o:
        output_writer = csv.writer(o)

        for el in elements:
            output_writer.writerow([(el)])


# takes a csv file and read each row into a list and prints
def read_csv(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        read_list = []
        header_row = next(reader)

        print(header_row)
        for row in reader:
            read_list.append(str(row))

        for el in read_list:
            print(el)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a program that reads and write in a csv file")

    parser.add_argument("-p", '--path', action="store_true", help='show path to csv file')
    parser.add_argument('-r', '--read', action="store_true", help="read content for csv file (-r)")
    parser.add_argument('-w', '--write', help="write content for csv file (-w 'content'). ")
    args = parser.parse_args()

    if args.path:
        print("ex1-cli.csv")

    if args.read:
        print_file_content("ex1-cli.csv")

    if args.write:
        write_elements_to_file("ex1-cli.csv", args.write)