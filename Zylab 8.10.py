# Erick Jimenez
# PSID: 1463639
# Zylab 8.10

if __name__ == '__main__':
    palindrome = input()
    regular = ""
    backwards = ""
    for ch in palindrome.lower():
        if ch != ' ':
            regular += ch
            backwards = ch + backwards
    if regular == backwards:
        print(palindrome + " is a palindrome")
    else:
        print(palindrome + " is not a palindrome")
