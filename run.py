import random

ingredient_list_one = ["potato", "tomato", "mushroom"]
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

lives = 4


def game_run():
    """
    Contains all functions needed to run the game. It also generate a computer choice
    of ingredients and print a welcome message. 
    """
    computer_first_choice = computer_choice_generator(ingredient_list_one)
    computer_second_choice = computer_choice_generator(ingredient_list_two)
    computer_third_choice = computer_choice_generator(ingredient_list_three)

    print('---------------------Feed the computer!--------------------------')
    print('-----------------------------------------------------------------')
    print('The machine would like a good soup. Can you guess what\
 to put in?\nChoose carefully your ingredients or it might not like it ...')
    print('-----------------------------------------------------------------')

    
    global lives

    def loose_game():
        """
        Function that is called when the user runs out of life
        """
        global lives
        lives = 4
        print('--------------------------------------------------------------')
        print('The computer was tired of waiting and ate you instead...sorry!')
        input('Press any key to restart\n')
        if input:
            game_run()
    
    def first_round():
        """
        Runs the first round of the game, display computer choice, takes user input
        and verify the answer. 
        """
        global lives

        print('Pick a first ingredient:')
        user_proposition_one = list_index(ingredient_list_one)
        user_input = input('You choose:\n>')

        if lives == 0:
            return loose_game()

        elif user_input in ingredient_list_one:
            if user_input == computer_first_choice:
                print(f"\nAlright! Let's start with a {user_input}")
                print('------------------------------------------------------')
                return second_round()

            else:
                lives = lives - 1
                print(f"\nOops, the machine is not in the mood for {user_input}.")
                print(f"Only {lives} lives left")
                print('------------------------------------------------------')
                first_round()
        else:
            print('\nThis ingredient is not in the list!')
            first_round()

    
    def second_round():
        """
        Runs the second round of the game, display computer choice, takes user input
        and verify the answer. 
        """
        global lives

        print('Pick an other ingredient:')
        user_proposition_two = list_index(ingredient_list_two)
        user_input = input('You choose:\n')

        if lives == 0:
            return loose_game()

        elif user_input in ingredient_list_two:
            if user_input == computer_second_choice:
                print("\nGood choice, You are a real gourmet!")
                print('------------------------------------------------------')
                return third_round()

            else:
                lives = lives - 1
                print(f"\nOops, the machine is not in the mood for {user_input}.")
                print(f"Only {lives} lives left")
                print('------------------------------------------------------')
                second_round()
        else:
            print('\nThis ingredient is not in the list!')
            second_round()
        

    def third_round():
        """
        Runs the third round of the game, display computer choice, takes user input
        and verify the answer. 
        """
        global lives

        print('And a last one:')
        user_proposition_three = list_index(ingredient_list_three)
        user_input = input('You choose:\n')


        if lives == 0:
            return loose_game()

        elif user_input in ingredient_list_three:
            if user_input == computer_third_choice:
                return win_game()

            else:
                lives = lives - 1
                print(f"\nOops, the machine is not in the mood for {user_input}.")
                print(f"Only {lives} lives left")
                print('------------------------------------------------------')
                third_round()
        else:
            print('\nThis ingredient is not in the list!')
            third_round()

    def win_game():
        """
        Function that is called if the game is won ,let the user being able to restart
        """
        global lives
        lives = 4
        print('--------------------------------------------------------------')
        print('Well done, It loves your soup !')
        print("You fed the computer, You get to live one more day.")
        input('Press enter to restart\n')

        if input:
            game_run()

    input('Press enter to start\n')

    if input:
        first_round()
game_run()