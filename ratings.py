"""Restaurant rating lister."""


# put your code here

def see_rated_restaurants(log_file):
    """Reading ratings from a file"""

    txt = open(log_file)

    ratings_dict = {}

    # new_restaurant = input("Enter a new restaurant.").title()
    # new_score = int(input("Enter the restaurant score."))

    # scores = [1,2,3,4,5]

    # if new_score not in scores:
    #     new_score = int(input("Rating must be between 1 and 5."))

    # print(f"New restaurant added : {new_restaurant}"
    #         f"Score: {new_score}")

    # ratings_dict[new_restaurant] = new_score

    for line in txt: #for every line in txt file
        line = line.rstrip() #get rid of /n
        words = line.split(":") #splt each element by the ":" into new list called words

        ratings_dict[words[0]] = words[1]

    for x,y in sorted(ratings_dict.items()):
        print(f"{x} is rated at {y}.")

    txt.close()


###########

def add_restaurants(log_file):
    """Add new restaurant & rating to file"""

    txt = open(log_file)

    ratings_dict = {}

    new_restaurant = input("Enter a new restaurant.").title()
    new_score = int(input("Enter the restaurant score."))

    scores = [1,2,3,4,5]

    if new_score not in scores:
        new_score = int(input("Rating must be between 1 and 5."))

    print(f"New restaurant added : {new_restaurant}"
            f"Score: {new_score}")

    ratings_dict[new_restaurant] = new_score

    for line in txt: #for every line in txt file
        line = line.rstrip() #get rid of /n
        words = line.split(":") #splt each element by the ":" into new list called words

        ratings_dict[words[0]] = words[1]

    for x,y in sorted(ratings_dict.items()):
        print(f"{x} is rated at {y}.")

    txt.close()
    
def user_choices():

    while True:

        choices = int(input("What would you like to do? "
                        "[1]See all ratings "
                        "[2]Add a new restaurant and rating "
                        "[3]Quit \n > "))

        if choices == 1:
            see_rated_restaurants("scores.txt")
            
        elif choices == 2:
            add_restaurants("scores.txt")
            print("Addition Success!")
            break
        elif choices == 3:
            print("Goodbye!")
            break
