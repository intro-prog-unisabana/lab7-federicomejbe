import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as f:
        password = f.read().strip()
    encrypt = caesar_encrypt(password)
    with open(filename, "w") as f:
        f.write(encrypt)




def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""

    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if row:
                rows.append(row)

    for index, row in enumerate(rows):
        if index > 0:  
            row[2] = caesar_encrypt(row[2])

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)



def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
        with open(filename, mode='r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if row:
                rows.append(row)

    found = False

    for index, row in enumerate(rows):
        if index > 0:
            if row[0] == website:
                row[2] = caesar_encrypt(password)
                found = True

    if found:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return True

    return False

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
