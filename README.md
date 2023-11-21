# PasswordManager

This is a terminal application that manages your passwords. It stores the passwords in an SQLite database and ciphers them based on a key you provide. Without the correct key, you get the wrong passwords, but you can still delete and add. The idea is that no one can read the passwords unless they know the key.

This is my first real project in Python. I started the project by using a CSV file to store the data, but then I figured out I would have to do lots of string handling because the ciphering of the text could introduce commas and spaces. So I decided to go with a database and stumbled upon SQLite, which is fun to use since I don't need a server for it.

As for the ciphering, I'm using what I believe is called the Vigenere ciphering method. However, I'm not just using it with letters and numbers. I'm using it with all unicode characters, so people who want to crack the key would have to go through all 1114111 unicode characters/codes to do so.

The project was lots of fun, and I definitely learned a lot.
