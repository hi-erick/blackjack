import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('blackjack_deck.db')

cursor = conn.cursor()

insert_card = '''INSERT INTO deck
                VALUES(?,?);
               '''
card = [ ('Seven of Hearts'), (7) ]
cursor.execute(insert_card, card)
cursor.close()
conn.commit()
conn.close()

# all cards have their number value except for face cards, their value is 10
# an ace can either be 1 or 11 depending on the hand