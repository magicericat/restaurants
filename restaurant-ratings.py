from sys import argv
script, file_name = argv


def alphabetize_restaurant_ratings(file_name):
    """Returns ratings in alphabetical order by restaurant.
    By Roo and Erica
    """

    restaurant_file = open(file_name)
    alpha_restaurants = {}

    for line in restaurant_file:
        line = line.strip()
        line = line.split(":")
        
        restaurant = line[0]
        rating = line[1]
        alpha_restaurants[restaurant] = rating

    restaurants = sorted(alpha_restaurants)

    for i in restaurants:
        print "%s is rated at %s." % (i, alpha_restaurants[i])


alphabetize_restaurant_ratings(file_name)



