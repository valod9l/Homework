"""Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.
To check your implementation you can use strings from here."""

base_string = input("Please, enter the text: ")


def palindrome(text_str):
    text_str = text_str.lower()
    if text_str == text_str[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(palindrome(base_string))
    print(palindrome("Kollok"))
