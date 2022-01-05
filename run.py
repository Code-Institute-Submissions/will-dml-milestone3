import random

ingredient_list_one = ["Potato","Tomato","Mushroom"]
ingredient_list_two = ["Oignon", "Cheese", "Wine"]
ingredient_list_three = ["Garlic", "Basilic", "Cilantro"]

def computer_choice_generator(data):
    """
    Get a random item from one of the list and return it
    """
    random_choice = random.choice(data)
    return random_choice

computer_first_choice = computer_choice_generator(ingredient_list_one)
computer_second_choice = computer_choice_generator(ingredient_list_two)
computer_third_choice = computer_choice_generator(ingredient_list_three)
print(computer_first_choice, computer_second_choice, computer_third_choice)

