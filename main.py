from fileinput import filename

from password_manager import add_login, change_password, encrypt_passwords_in_file


def main():
    filename = input("Enter the CSV file name: ")
    encrypt_passwords_in_file(filename)

    while True:
        option = input("Options: (1) Change Password, (2) Add Password, (3) Quit: ")
        if option == "1":
            data = input("Enter the website and the new password: ").split()
            if len(data) != 2:
                print("Input is in the wrong format!")
                continue
            website = data[0]
            new_password = data[1]
            if len(new_password) < 12:
                print("Password is too short!")
                continue
            result = change_password(filename, website, new_password)
            if result is False:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")
        elif option == "2":
            data = input("Enter the website, username, and password: ").split()
            if len(data) != 3:
                print("Input is in the wrong format!")
                continue
            website = data[0]
            username = data[1]
            password = data[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, password)
            print("Login added.")
        elif option == "3":
            break
        else:
            print("Invalid option selected!")
if __name__ == "__main__":
    main()