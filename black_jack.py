#if player's hand is an ace and a face card, player automatically wins this is called a natural
#same for dealer
#if faceup card of dealer is a face or ace it checks the hidden card for possible natural
import sqlite3

#draws a card from the deck
draw_card = ''' SELECT * FROM deck
                ORDER BY random()
                LIMIT 1;
            '''
#card drawn from deck is removed so it can't be drawn again
remove_from_deck =  ''' DELETE FROM deck
                       WHERE id = ?;
                    '''
#insert all removed decks back into deck(database)
insert_into_deck = ''' INSERT INTO deck
                    VALUES(?, ?);
                '''


# cursor.execute(draw_card)
# card = cursor.fetchone()
# drawn_cards.append(card)
# cursor.execute(remove_from_deck, (card[0],) )

class Dealer():
    def __init__(self):
        self.hand = []
        self.value

class Player():
    def __init__(self):
        self.hand = []
        self.value 

def take_card(self):





if __name__=='__main__':
    conn = sqlite3.connect('blackjack_deck.db')
    drawn_cards = []
    cursor = conn.cursor()
    
    dealers_hand = []
    players_hand = []

    cursor.executemany(insert_into_deck, drawn_cards)
    cursor.close()
    conn.commit()