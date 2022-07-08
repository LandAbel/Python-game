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

    def calculated_trap_attack():
        return randint(trap['tattack_min'], trap['tattack_max'])
        
    def calculate_player_attack():
        return randint(player['attack_min'], player['attack_max'])
    
    print('---' * 7)
    print('Please enter username:\n')
    player['name'] = input()
    print('\n Welcome in the another world.\n I hope you enjoy the game.\n')
    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(' ')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    helper=True
    if helper == True:
        print('\n' + '---' * 7)
        print('Please enter your action:\n')
        print(' 1) Attack \n 2) Heal\n 3) Extra skill\n 4) Trick skill\n 5) Run\n 6) Show Results\n 7) User manual\n 8) Exit game\n')
        print('---' * 7)
        helper=False

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False
                
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
                        print("\n If you wanna use the other skill press 2.\n")
                    
                elif player_choice2 == '2'and one_time2 == True:
                    monster['health'] = monster['health'] - 50
                    one_time2 = False
                    print("You used the extra damage skill.")
                    if one_time == True:
                        print("\n If you wanna use the other skill press 1.\n")
                    
            else:
                print("\n Sorry you used all the extra skill.\n")
                  

        elif player_choice == '4': 
                player['health'] = player['health'] - 14 
                monster['health'] = monster['health'] - calculate_player_attack()

        elif player_choice == '5':
            player['health'] = player['health'] - calculated_trap_attack()

        elif player_choice == '6':
            for player_stat in game_results:
                print('\n Last match won by:', player_stat)

        elif player_choice == '7':
            print('If you type 1, your caracter hit the monster after that a monster hit you back.\n If you type 2, your caracter heal hear/himself, but the monster hit you and he get 5 more hp.\n If you type 3, you can choose from the extra skill list.\n If you type 4, you can choose from the trick skill list.\n If you type 5, you can choose from the trap skill list.\n If you type 6, you can see the last match result.\n If you type 7, you can see the user manual.\n If you type 8, you can exit the game.\n')

        elif player_choice == '8':
            print('\nThanks for your time.\n')
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
        print('\n Congratulation you destroyed the MONSTER')

    if monster_won == True:

        print('\n Next time might be able to destroy the MONSTER')


