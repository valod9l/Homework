"""2.2) Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function."""

a = "I am global variable!"


def enclosing_function():

    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    inner_function()


if __name__ == "__main__":
    enclosing_function()
