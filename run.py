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

    while True:
        if lives == 0:
            break
         
        def first_round():
            global lives

            print('Pick an ingredient:')
            user_proposition_one = list_index(ingredient_list_one)
            user_input = input('You take this:\n')

            if user_input in ingredient_list_one:
                if user_input == computer_first_choice:
                    print('\nGood!')
                    return

                else:
                    lives = lives - 1
                    print('\n Not gooood, you havelives left')
                    print(lives)
                    first_round()
            else:
                print('\nWe did not understand what you meant bruuuuuh')
                first_round()

        first_round()
        
        def second_round():
            global lives

            print('Pick an other ingredient:')
            user_proposition_two = list_index(ingredient_list_two)
            user_input = input('You take this:\n')

            if user_input in ingredient_list_two:
                if user_input == computer_second_choice:
                    print('\nGood!')
                    return

                else:
                    lives = lives - 1
                    print('\n Not gooood, you havelives left')
                    print(lives)
                    second_round()
            else:
                print('\nWe did not understand what you meant')
                second_round()
            
        second_round()

        def third_round():
            global lives

            print('And a last one:')
            user_proposition_three = list_index(ingredient_list_three)
            user_input = input('You take this:\n')

            if user_input in ingredient_list_three:
                if user_input == computer_third_choice:
                    print('\nCongrats!')
                    return

                else:
                    lives = lives - 1
                    print('\n Not gooood, you havelives left')
                    print(lives)
                    third_round()
            else:
                print('\nWe did not understand what you meant')
                third_round()
            
        third_round()
game_run()


    