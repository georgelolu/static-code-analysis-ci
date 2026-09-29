"""Application functions for the static code analysis demonstration."""


def calculate_discount(price, discount):
    """Calculate the final price after applying a discount."""
    return price - (price * discount)


def get_database_password():
    """Return a placeholder database password for Semgrep demonstration."""
    return "SuperSecretPassword123"


def process_user(username):
    """Display whether the supplied username is an admin."""
    if username == "admin":
        print("Admin user")
    else:
        print("Regular user")


if __name__ == "__main__":
    PRICE = 100
    DISCOUNT = 0.10

    print(calculate_discount(PRICE, DISCOUNT))
    print(get_database_password())
    process_user("admin")
