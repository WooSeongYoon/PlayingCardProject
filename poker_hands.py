from enum import IntEnum



class Card:
    def __init__(self, pattern, character):
        self.pattern=pattern
        self.character=character
    pattern=''
    character=''

class Rank(IntEnum):
    High_Card=1
    One_Pair=2
    Two_Pairs=3
    Three_of_a_Kind=4
    Straight=5
    Flush=6
    Full_House=7
    Four_of_a_Kind=8
    Straight_Flush=9
    Royal_Straight_Flush=10

class Player:
    rank:Rank
    sub_rank:int

    def __init__(self, name):
        self.name=name
        self.cards=[]
        self.characters=[]
        self.patterns=[]

    def get_cards(self, *cards:Card):
        for card in cards:
            self.cards.append(card)
            self.characters.append(character_to_number(card.character))
            self.patterns.append(card.pattern)
        self.characters.sort()
        self.patterns.sort()
    def get_dealer_cards(self, cards:tuple):
        for card in cards:
            self.cards.append(card)
            self.characters.append(character_to_number(card.character))
            self.patterns.append(card.pattern)
        self.characters.sort()
        self.patterns.sort()

    def print_cards(self):
        str=self.name+' cards : '
        for card in self.cards:
            str+=f'{card.pattern} {card.character}, '
        print(str)
        str=self.name+' characters : '
        for character in self.characters:
            str+=f'{number_to_character(character)}, '
        print(str)
        str=self.name+' patterns : '
        for pattern in self.patterns:
            str+=f'{pattern}, '
        print(str)

def character_to_number(character:str):
    if character=='A':
        return 1
    elif character=='2':
        return 2
    elif character=='3':
        return 3
    elif character=='4':
        return 4
    elif character=='5':
        return 5
    elif character=='6':
        return 6
    elif character=='7':
        return 7
    elif character=='8':
        return 8
    elif character=='9':
        return 9
    elif character=='10':
        return 10
    elif character=='J':
        return 11
    elif character=='Q':
        return 12
    elif character=='K':
        return 13
    else:
        raise Exception('Invalid character for card')

def number_to_character(number:int):
    if number>=2 and number<=10:
        return str(number)
    elif number==1:
        return 'A'
    elif number==11:
        return 'J'
    elif number==12:
        return 'Q'
    elif number==13:
        return 'K'
    else:
        raise Exception('Invalid number for card')
    
def get_rank(player:Player):
    rank = Rank.High_Card
    for card in player.cards:
        character_to_number(card.character)

    if(len(player.cards)>=2):
        if(is_one_pair(player)):
            rank=Rank.One_Pair
    if(len(player.cards)>=4):
        if(is_two_pairs(player)):
            rank=Rank.Two_Pairs
    if(len(player.cards)>=3):
        tf,_=is_three_of_a_kind(player)
        if(tf):
            rank=Rank.Three_of_a_Kind
    if(len(player.cards)>=5):
        if(is_straight(player)):
            rank=Rank.Straight
        if(is_flush(player)):
            rank=Rank.Flush
        if(is_full_house(player)):
            rank=Rank.Full_House
        if(is_four_of_a_kind(player)):
            rank=Rank.Four_of_a_Kind
        if(is_straight(player) and is_flush(player)):
            if(player.characters[0]==1 and player.characters[1]==10):
                rank=Rank.Royal_Straight_Flush
            else:
                rank=Rank.Straight_Flush
    return rank


def is_straight(player:Player):
    for i in range(0,2):
        if(player.characters[i]+4
        ==player.characters[i]+3
        ==player.characters[i]+2
        ==player.characters[i]+1
        ==player.characters[i]):
            return True
    if(1 in player.characters and 10 in player.characters and 11 in player.characters and 12 in player.characters and 13 in player.characters ):
        return True
    return False

def is_full_house(player:Player):
    tf,ch = is_three_of_a_kind(player)
    if(tf):
        temp=player.characters.copy()
        while(ch in temp):
            temp.remove(ch)
        for i in temp:
            if(temp.count(i)==2):
                return True
    return False

def is_flush(player:Player):
    for i in range(0,2):
        if(player.patterns[i]==player.patterns[i+1]==player.patterns[i+2]==player.patterns[i+3]==player.patterns[i+4]):
            return True
        else:
            return False

def is_four_of_a_kind(player:Player):
    for character in player.characters:
        if(player.characters.count(character)==4):
            return True
    return False

def is_three_of_a_kind(player:Player):
    for character in player.characters:
        if(player.characters.count(character)==3):
            return True, character
    return False, 'no'

def is_two_pairs(player:Player):
    for character in player.characters:
        if(player.characters.count(character)==2):
            x=character
            for character in player.characters:
                if(player.characters.count(character)==2):
                    y=character
                    if (x!=y):
                        return True
    return False

def is_one_pair(player:Player):
    for character in player.characters:
        if(player.characters.count(character)==2):
            return True
    return False

def win_lose(player1:Player, player2:Player):
    draw = 'draw'
    if(get_rank(player1)>get_rank(player2)):
        return player1
    elif(get_rank(player1)<get_rank(player2)):
        return player2
    elif(get_rank(player1)==get_rank(player2)):
        if(len(player1.characters)>=5 and len(player2.characters)>=5):
            if(get_rank(player1)==Rank.Straight_Flush):
                if(player1.characters[0]>player2.characters[0]):
                    return player1
                elif(player1.characters[0]<player2.characters[0]):
                    return player2
                else:
                    return draw
            elif(get_rank(player1)==Rank.Four_of_a_Kind or Rank.Full_House):
                if(player1.characters[2]>player2.characters[2]):
                    return player1
                elif(player1.characters[2]<player2.characters[2]):
                    return player2
                else:
                    return draw
            elif(get_rank(player1)==Rank.Flush or Rank.Straight):
                if(player1.characters[4]>player2.characters[4]):
                    return player1
                elif(player1.characters[4]<player2.characters[4]):
                    return player2
                else:
                    return draw
        if(len(player1.characters)>=3 and len(player2.characters)>=3):
            if(get_rank(player1)==Rank.Three_of_a_Kind):
                if(player1.characters[2]>player2.characters[2]):
                    return player1
                elif(player1.characters[2]<player2.characters[2]):
                    return player2
                else:
                    return draw
        if(len(player1.characters)>=4 and len(player2.characters)>=4):
            if(get_rank(player1)==Rank.Two_Pairs):
                for character in player1.characters:
                    if(player1.characters.count(character)==2):
                        player1x=character
                        for character in player1.characters:
                            if(player1.characters.count(character)==2):
                                player1y=character
                                if player1x!=player1y:
                                    break
                for character in player2.characters:
                    if(player2.characters.count(character)==2):
                        player2x=character
                        for character in player2.characters:
                            if(player2.characters.count(character)==2):
                                player2y=character
                                if player2x!=player2y:
                                    break
                if(player1y>player2y):
                    return player1
                elif(player1y<player2y):
                    return player2
                elif(player1x>player2x):
                    return player1
                elif(player1x<player2x):
                    return player2
                else:
                    return draw
        if(len(player1.characters)>=2 and len(player2.characters)>=2):
            if(get_rank(player1)==Rank.One_Pair):
                for character in player1.characters:
                    if(player1.characters.count(character)==2):
                        x=character
                for character in player2.characters:
                    if(player1.characters.count(character)==2):
                        y=character
                if(x>y):
                    return player1
                elif(x<y):
                    return player2
                else:
                    return draw
        if(len(player1.characters)>=1 and len(player2.characters)>=1):
            if(get_rank(player1)==Rank.High_Card):
                if(player1.characters[len(player1.characters)-1]>player2.characters[len(player2.characters)-1]):
                    return player1
                elif(player1.characters[len(player1.characters)-1]<player2.characters[len(player2.characters)-1]):
                    return player2
                else:
                    return draw

def main():
    player1=Player('asdf')
    player2=Player('qwer')

    player1.get_cards(Card('Clover','3'), Card('Clover','7'), Card('Clover','4'), Card('Clover','8'), Card('Spade','5'), Card('Clover','2'), Card('Spade','6'))
    player2.get_cards(Card('Spade','A'), Card('Clover','K'), Card('Clover','A'), Card('Clover','4'), Card('Diamond','4'), Card('Clover','4'), Card('Heart','K'))
    
    player1.print_cards()
    player2.print_cards()
    print(f'{player1.name} : {get_rank(player1).name}, {player2.name} : {get_rank(player2).name}')
    print(f'{win_lose(player1,player2).name} wins')

if __name__ == "__main__":
    main()
