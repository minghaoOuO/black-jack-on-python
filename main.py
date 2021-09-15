while True:
    # initialize data
    player_card =[]
    com_card = []
    # both player and com draw two cards
    draw(com_card)
    show_card_com_1()  
    draw(com_card)
    draw(player_card)
    draw(player_card)
    show_card_player()
    # count how many cards have drawn from deck
    h_count_player = 0
    h_count_com = 0
    
    while True:#player hit
        print("please choose, (H = Hit , (S = Stand")
        act = input()
        if act == "H":
            draw(player_card)
            show_card_com_1()
            show_card_player()
            h_count_player += 1
            if check_more_than_21(player_card):
                break
        else:
            break
        if h_count_player == 3:
            print("You already have 5 cards")
            break
    
    # check if player's point bigger than 21
    if count_points(player_card) <= 21:
        while True:#com_hit
            if count_points(com_card) < 17 and h_count_com < 3:
                draw(com_card)
                h_count_com += 1
            else:
                break
        
    else:
        end_print()
        print("U Lose")
    
    # check if com's point bigger than 21
    if count_points(com_card) > 21:
        end_print()
        print("U Win")
        
    # check if get five cards to win
    if h_count_player == 5 and count_points(player_card) <= 21:
        if h_count_com == 5 and count_points(com_card) <= 21:
            end_print()
            print("Even")
        else:
            end_print()
            print("U Win")
    
    # then find whose point is bigger
    if count_points(com_card) <= 21 and count_points(player_card) <= 21:
        if count_points(com_card) > count_points(player_card):
            end_print()
            print("U lose")
        elif count_points(com_card) < count_points(player_card):
            end_print()
            print("U Win")
            
        else:
            end_print()
            print("Even")
            
    # ask if playing again?
    print("GG!!Wanna play again??(Y)/(N)")
    react = input()
    if react == "N":
        print('Thanks for playing this game,bye~')
        break 
        
