from random import randint

game_running = True
game_results = []
one_time = True
one_time2 = True
one_time_game = True

def calculate_monster_attack(attack_min, attack_max):
     return randint(attack_min, attack_max)

def calculate_player_heal(heal_min, heal_max):
     return randint(heal_min, heal_max)

def game_ends(winner_name):
    print(f'{winner_name} won the game')

    

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Abel', 'attack_min': 5, 'attack_max': 30, 'heal_min': 16, 'heal_max': 30, 'health': 100}
    monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 28, 'health': 200}
    trap = {'tattack_min':0, 'tattack_max':20}
    potion = {'min': 20, 'max': 50}
    starter_money =200

    def calculated_trap_attack():
        return randint(trap['tattack_min'], trap['tattack_max'])
    
    def potion_health_reg():
        return randint(potion['min'],potion['max'])
    
    def calculate_player_attack():
        return randint(player['attack_min'], player['attack_max'])

    print('---' * 7)
    print('Please enter username:')
    print(' ')
    player['name'] = input()
    print(' ')
    print('Welcome in the another world.')
    print(' ')
    print('I hope you enjoy the game')
    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(' ')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False
        print('''
        Please select action:\r\n
        1) Attack\r\n
        2) Heal\r\n
        3) Extra skill\r\n
        4) Trick skill\r\n
        5) Run\r\n
        6) Show Results\r\n
        7) User manual\r\n
        8) Exit game
        ''')
        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack()
            if monster['health'] <= 0:
                player_won = True
            
            else:
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True
            
        elif player_choice == '2':
            player['health'] = player['health'] + calculate_player_heal(player['heal_min'], player['heal_max'])
            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True
            if player_choice == '2':
             monster['health'] = monster['health'] + 5

        elif player_choice == '3':   
            while one_time == True or one_time2 == True:
                print('1) Heal up with 30 hp')
                print('2) Decrease monster health with 50 hp ')
                player_choice2 = input()
                if player_choice2 == '1' and one_time == True:
                    player['health'] = player['health'] + 30
                    one_time = False 
                    print("You used the extra heal skill.")
                    if one_time2 == True:
                        print(' ')
                        print("If you wanna use the other skill press 2.")
                        print(' ')
                    
                elif player_choice2 == '2'and one_time2 == True:
                    monster['health'] = monster['health'] - 50
                    one_time2 = False
                    print("You used the extra damage skill.")
                    if one_time == True:
                        print(' ')
                        print(" If you wanna use the other skill press 1.")
                        print(' ')
                    
            else:
                print(' ')
                print("Sorry you used all the extra skill")
                print(' ')
                  

        elif player_choice == '4': 
                player['health'] = player['health'] - 14 
                monster['health'] = monster['health'] - calculate_player_attack()

        elif player_choice == '5':
            player['health'] = player['health'] - calculated_trap_attack()

        elif player_choice== '6':
            if starter_money >= 100:
                player['helath'] = player['health'] - potion_health_reg()
                starter_money -= 100
            else:
                print('You need to collect more money to buy this item') 
            
        elif player_choice == '7':
            for player_stat in game_results:
                print(' ')
                print('Last match won by:', player_stat)
                print(' ')


        elif player_choice == '8':
            print('If you type 1, your caracter hit the monster after that a monster hit you back.')
            print(' ')
            print('If you type 2, your caracter heal hear/himself, but the monster hit you and he get 5 more hp.')
            print(' ')
            print('If you type 3, you can choose from the extra skill list.')
            print(' ')
            print('If you type 4, your caracter start running from the monster, but you can get hit by the trap.')
            print(' ')
            print('If you type 5, you able to see a previous round stats(winner name, rest of health, and number of round.')
            print(' ')
            print('If you type 6, you can see the user manual.')
            print(' ')
            print('If you type 7, the game ends automatically.')
            print(' ')
            print('If anything not work correctly please send a message to me.')
            print(' ')

        elif player_choice == '9':
            print(' ')
            print('Thanks for your time.')
            print(' ')
            new_round = False
            game_running = False

        else:
            print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' hp left')
            print('----' * 7)
            print(monster['name'] + ' has ' + str(monster['health']) + ' hp left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won: 
            game_ends(monster['name'])
            round_result = {'name': monster['name'], 'health': monster['health'], 'round' : counter}
            game_results.append(round_result)
            new_round = False
        
    if player_won == True:
        print(' ')
        print('Congratulation you destroyed the MONSTER')

    if monster_won == True:
        print(' ')
        print('Next time might be able to destroy the MONSTER')


