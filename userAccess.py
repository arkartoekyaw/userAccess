import json

db = {}


def main_sector():
    while True:
        try:
            main_option = int(input("Press 1 to Register:\nPress 2 to Login\nPress 3 to Exit:"))
            if main_option == 1:
                registration()
            elif main_option == 2:
                login()
            elif main_option == 3:
                recording_all_data()
                exit(1)
            else:
                print("Invalid Option")
                main_sector()
                continue
        except ValueError:
            print("Please enter only integers.")
            continue



def registration():
    user_email = input("Enter your email:")

    if email_exists(user_email, db):
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        user_phone = int(input("Enter your phone:"))
        user_age = int(input("Enter your age:"))

        id = len(db)

        to_insert = {id: {"email": user_email, "u_name": user_name, "password": user_password, "phone": user_phone,
                          "age": user_age}}
        db.update(to_insert)


def login():
    user_found = -1
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")

    for key, value in db.items():
        if value["email"] == l_user_email and value["password"] == l_user_password:
            user_found = key

    if user_found != -1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("User not Found!!!")


def user_profile(user_found):
    print("Welcome:",db[user_found]["u_name"])

    while True:
        try:
            option = int(input("Press 1 to exit:\nPress 2 to update your infos:"))
            if option == 1:
                recording_all_data()
                exit(1)
            elif option == 2:
                update_user_infos(user_found)
            else:
                print("Invalid Option")
                user_profile(user_found)
                continue
        except ValueError:
            print("Please enter only integers.")
            continue


def email_exists(email, db):
    for user_id, user_email in db.items():
        if user_email['email'] == email:
            return True
    return False

# def update_user_infos():
#     pass

def update_user_infos(user_id):
    print("Enter new information (leave blank if no change):")
    new_email = input("Email: ") or db[user_id]["email"]
    new_name = input("Name: ") or db[user_id]["u_name"]
    new_password = input("Password: ") or db[user_id]["password"]
    new_phone = input("Phone: ") or db[user_id]["phone"]
    new_age = input("Age: ") or db[user_id]["age"]
    
    db[user_id] = {"email": new_email, "u_name": new_name, "password": new_password, "phone": new_phone, "age": new_age}
    print("User information updated.")

def recording_all_data():
    with open("record.txt", 'w') as file:
        file.write(json.dumps(db))


def loading_all_data():
    try:
        with open('record.txt') as file:
            data = json.load(file)
            db.update(data)
    except FileNotFoundError:
        pass



if __name__ == '__main__':

    loading_all_data()
    # print(db)

    while True:
        main_sector()