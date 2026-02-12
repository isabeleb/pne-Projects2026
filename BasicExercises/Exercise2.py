#The string with leading and trailing spaces removed (use strip())
#The number of words in the string (use split())
#The string with the first letter of each word capitalized (use title())
#Whether the stripped string starts with "Hello" (use startswith())
#Whether the stripped string ends with "ing." (use endswith())
#The position (index) of the word "Python" in the stripped string(use find())
#The words joined back together separated by " - " (use split() and " - ".join())

text = "  Hello, World! Welcome to Python Programming.  "

print("Text with no leading/trailing spaces:" , text.strip(" "))

words_list = text.split()
print("Word count:" , len(words_list))

print("Capitalized:" , text.title())