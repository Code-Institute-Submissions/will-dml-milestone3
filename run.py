import random

ingredient_list_one = ["potato","tomato","mushroom"]
ingredient_list_two = ["oignon", "cheese", "wine"]
ingredient_list_three = ["garlic", "basilic", "cilantro"]

def list_index(list):
    """
    Iterate throught a list and print it.
    """
    for i in list:
        print(i)

def computer_choice_generator(data):
    """
    Get a random item from one of the list and return it
    """
    random_choice = random.choice(data)
    return random_choice

computer_first_choice = computer_choice_generator(ingredient_list_one)
computer_second_choice = computer_choice_generator(ingredient_list_two)
computer_third_choice = computer_choice_generator(ingredient_list_three)


lives = 4


def game_run():
    print('-------------Feed the computer------------------' )
    print('Guess what he wants before he eat you lives left.')
    print('--------------------------------------------------')
    """
    Print first list of ingredients, takes user input and verify it
    """
    
    global lives

    def loose_game():
        global lives
        lives = 4
        print('--------------------------------------------------------------')
        print('The computer was tired of waiting and ate you instead...sorry!')
        input('Press any key to restart')
            
        if input:
            game_run()
            
        
         
    def first_round():
        global lives

        print('Pick an ingredient:')
        user_proposition_one = list_index(ingredient_list_one)
        user_input = input('You take this:\n>')

        if lives < 1:
            return loose_game()

        elif user_input in ingredient_list_one:
            if user_input == computer_first_choice:
                print('\nGood!')
                print('--------------------------------------------------------')
                return

            else:
                lives = lives - 1
                print(f'\nPuuaa! It does not like that, you have {lives} lives left')
                print('--------------------------------------------------------')
                first_round()
        else:
            print('\nThis ingredient is not in the list!')
            first_round()

    first_round()
    
    def second_round():
        global lives

        print('Pick an other ingredient:')
        user_proposition_two = list_index(ingredient_list_two)
        user_input = input('You take this:\n')

        if lives < 1:
            return loose_game()

        elif user_input in ingredient_list_two:
            if user_input == computer_second_choice:
                print('\nGood!')
                print('--------------------------------------------------------')
                return

            else:
                lives = lives - 1
                print(f'\nPuuaa! It does not like that, you have {lives} lives left')
                print('--------------------------------------------------------')
                second_round()
        else:
            print('\nThis ingredient is not in the list!')
            second_round()
        
    second_round()

    def third_round():
        global lives

        print('And a last one:')
        user_proposition_three = list_index(ingredient_list_three)
        user_input = input('You take this:\n')

        if lives < 1:
            return loose_game()

        elif user_input in ingredient_list_three:
            if user_input == computer_third_choice:
                print('\nCongrats!')
                return

            else:
                lives = lives - 1
                print(f'\nPuuaa! It does not like that, you have {lives} lives left')
                print('--------------------------------------------------------')
                third_round()
        else:
            print('\nThis ingredient is not in the list!')
            third_round()
        
    third_round()
    
        

game_run()


    