def remove_fourth_character(word: str) -> str:
    mess = word[:3]
    mess_2 = word[4:]
    new_mess = mess + mess_2
    return new_mess




# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
