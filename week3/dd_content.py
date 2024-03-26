import csv
import random
from collections import defaultdict

def get_random_qoute(myqoutes='qoutes.csv'):
    try:
        with open(myqoutes, 'r') as filehandle:
            reader = csv.reader(filehandle, delimiter='|')
            list_dict = [{'author' : row[0], 'qoute':row[1]} for row in reader]

    except  Exception as e:
        print("Failure is not the end. It's just another step closer to success.")
        list_dict = [{'author' : 'uhlulekile', 'qoute':'ngeke kulunge'}]

    return random.choice(list_dict)

def get_weather_forecase():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass


if  __name__ == "__main__":
    print('Testing qoute generation ')

    qoute = get_random_qoute()
    print(f' - Random qoute is "{qoute["qoute"]}" - {qoute["author"]}')

    qoute = get_random_qoute(myqoutes=None)
    print(f' - Default qoute is "{qoute["qoute"]}" - {qoute["author"]}')