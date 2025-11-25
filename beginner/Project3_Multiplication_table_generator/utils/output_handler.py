# Handles display and file-saving logic
def display_table(table):
    for line in table:
        print(line)


def save_table_to_file(table, filename):
    with open(filename, "w") as file:
        for line in table:
            file.write(line + "\n")
