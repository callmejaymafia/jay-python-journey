# Core logic for generating the table


def generate_multiplication_table(n, start, end):
    table = []
    for i in range(start, end + 1):
        table.append(f"{n} x {i} = {n * i}")
    return table
