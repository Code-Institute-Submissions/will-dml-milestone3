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

print('-------------Feed the computer------------------' )
print('Guess what he wants before he eat you lives left.')
print('--------------------------------------------------')



def first_round():
    print('Pick an ingredient:')
    user_proposition_one = list_index(ingredient_list_one)
    user_input = input('You take this:\n')

    if user_input in ingredient_list_one:
        if user_input == computer_first_choice:
            print('\nGood!')
        else:
            print('\nNot gooood')
            first_round()
    else:
        print('\nWe did not understand what you meant')
        first_round()

first_round()



    