'''
    A python implementation of Bruce Schneier's Solitaire Algorithm from
    Neil Stevenson's cryptonomicon
    Assumptions: Full deck of cards, therefore we will use bridge order (clubs, diamonds, hearts, spades)
'''


def letterToNumber(letter):
    #Convert letter to its related number (A = 1, B = 2, etc)
    if letter in letters:
        return ord(letter.upper()) - 64)
    return 0

def NumberToLetter(number):
    #convert number to its related letter
    letter = chr(((number - 1) % 26) + 65)
    return letter
    
class Solitaire:
    def _defaultDeck(cardSet):
        #Default Deck Order for when you lack a key
        
        cardSet.deck = []
        for cardNum in range(1, 55):
            cardSet.deck = cardSet.deck + [cardNum]
    
    def _KeyDeck(cardSet, key):
        #Change order based on key