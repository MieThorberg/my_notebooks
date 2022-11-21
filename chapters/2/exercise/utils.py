import os


# takes a path to a folder
# and writes all filenames in the folder to a specified output file
def get_file_names(folderpath, out='ex2-output.txt'):
    file_names = os.listdir(folderpath)

    with open(out, 'w') as file:
        file.write(str(file_names))


# takes a path to a folder
# and write all filenames recursively (files of all sub folders to)
def get_all_file_names(folderpath,out='ex2-output.txt'):
    file_names = os.listdir(folderpath)

    with open(out, 'w') as file:
        for file_name in file_names:
            print(file_name)
            full_path = os.path.join(str(folderpath), str(file))
            if os.path.isdir(full_path):
                print("is dir")
                get_all_file_names(full_path)
            else:
                print("file folder:" + folderpath)
                file.write(file_name + ", ")


# takes a list of filenames and print the first line of each
# def print_line_one(file_names):
#    pass

# takes a list of filenames
# and print each line that contains an email (just look for @)
# def print_emails(file_names):
#    pass

# takes a list of md files
# and writes all headlines (lines starting with #) to a file
# def write_headlines(md_files, out=output.txt):
#    pass

get_file_names('/home/jovyan/my_notebooks/Exercises/02-Exercise')
get_all_file_names('/home/jovyan/my_notebooks')
