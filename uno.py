def start_game():
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = (list(range(1,11)))

    deck = [(colour,rank) for colour in colours for ranks in rank]

    random.shuffle(deck)

    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck [14:]

    #central card

    central_card = deck.pop[0]

    main_loop(p1, p2, deck, central_card, 0)

    def main_loop(p1, p2, deck, central_card, whose_turn):

        while  p1 and p2:
            print(f"players turn: {whose_turn + 1}, players hand : {p1}")
            print(f"Central_card: {central_card}")

            # give a choice , play a card or draw card

            ans = int(input("You have a choice. You can draw(0) or play (1)"))

            if ans == 1:
                player_choice = int(input("which card do you want to play?")) -1 
                valid =valid_play(cental_card, p1[player_choice])
                if valid:
                    central_card = p1.pop(player_choice)

            if not(ans):
                p1.append(deck.pop(0))
                p1, p2 = p2, p1
                whose_turn = (whose_turn + 1) % 2

def valid_play(card1, card2):
        return(card1[0] == card2[1] or card1[1] == card2[1])
