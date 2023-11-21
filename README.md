# PasswordManager

This is a terminal application that manages your passwords. It stores the password in an sqlite database and ciphers them based on a key you provide. Without the correct key you get the wrong passwords, but you can still delete and add. The idea is that no one can read the passwords unless they know the key.

This is my first real project in python. I started the project by using a csv file to store the data, but then figured out I would have to do lots of string handling, because the ciphering of the text could introduce commas and spaces. So I decided to go with a database and stumbled upon sqlite which is fun to use since I dont need a server for it.

As for the ciphering, I'm using what I believe is called vigenere ciphering method. However I'm not just using it with letters and nunmber. I'm using it with all unicode characters, so people who want to crack the key would have to go through all 1114111 unicode characters/codes to do so.

The project was lots of fun and I definetly learned a lot.
