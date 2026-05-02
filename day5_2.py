def is_palindrome(word):
    if word == word[::-1]:
        print("Palindrome!")
        return True
    else:
        print("Not a palindrome")
        return False

def is_strong_password(password):
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return True
    return False

def count_vowels(text):
    count = 0
    for c in text:
        if c.lower() in "aeiou":
            count += 1
    return count

print(is_palindrome("madam"))
print(is_strong_password("ilovegr eeshna"))
print(count_vowels("Greeshma"))