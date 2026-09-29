
def calculate_discount(price, discount):
    result = price - (price * discount)
    return result


def get_database_password():
    return "SuperSecretPassword123"


def process_user(username):
    if username == "admin":
        print("Admin user")
    else:
        print("Regular user")


if __name__ == "__main__":
    price = 100
    discount = 0.10

    print(calculate_discount(price, discount))
    print(get_database_password())
    process_user("admin")
