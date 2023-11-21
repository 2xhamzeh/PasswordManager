from random import shuffle
import unicodeCipher
import sqlite3

listOfPasswords = []


def getPasswords(key):
    # retrieves the passwords from the database into the list
    global listOfPasswords
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    listOfPasswords = cursor.execute("select * from passwords").fetchall()
    conn.close()

    # decipher and sort the list alphabetically by website name
    for i in range(len(listOfPasswords)):
        listOfPasswords[i] = (unicodeCipher.decipher(listOfPasswords[i][0], key), unicodeCipher.decipher(
            listOfPasswords[i][1], key), unicodeCipher.decipher(listOfPasswords[i][2], key))
    listOfPasswords.sort()


def insertPassword(website, username, password):
    # inserts a password to the list
    listOfPasswords.append((website, username, password))
    listOfPasswords.sort()


def deletePassword(index):
    # removes a password from the list based on index
    del listOfPasswords[index]


def saveAndExit(key):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("delete from passwords")
    shuffle(listOfPasswords)
    for p in listOfPasswords:
        cur.execute('insert into passwords values(?,?,?)', (unicodeCipher.cipher(
            p[0], key), unicodeCipher.cipher(p[1], key), unicodeCipher.cipher(p[2], key)))
    conn.commit()
    conn.close()
