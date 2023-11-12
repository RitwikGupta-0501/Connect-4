import pickle
import sys


# Checks if user exists
# Accesses and Displays details of a user
def get_user_details(user):
    """
    * Accesses the details.dat file and searches for users.\n
    * Then displays their details.\n
    Parameters -
        users --> A list of Users
    """
    details = open("./files/details.dat", 'rb')
    temp = []
    while True:
        try:
            data = pickle.load(details)
            temp.append(data)

            if user == data[0]:
                return data

        except EOFError:
            if 'UNknowN' == user:
                for i in temp:
                    print(i)
                sys.exit("Bye Boss ;)")
            else:
                details.close()
                del temp
                return 'User Does Not Exist.'


# Updates players.txt with New Player Names
def make_player(users):
    """
    * Writes Usernames of Players in players.txt file to Allow game.py to access them.\n
    * Also creates a new entry in details.dat IF it Doesn't Exist.\n
    Parameters -
        user_no --> The N'th User we are logging in.
        username --> User ID of the player.
    """
    players = open("./files/players.dat", 'wb')
    pickle.dump({'red': users[0], 'yellow': users[1]}, players)
    players.close()

    details = open("./files/details.dat", "rb+")
    for i in range(2):
        while True:
            try:
                data = pickle.load(details)
                if data[0] == users[i]:
                    details.seek(0)
                    break
            except EOFError:
                pickle.dump([users[i], 0, 0, 0], details)
                details.seek(0)
                break
    details.close()
    return


import pickle


# Update Player Details
def update_player_details(winner, loser, draw=False):
    details = open("./files/details.dat", "rb+")
    while True:
        try:
            pos = details.tell()
            data = pickle.load(details)
            if data[0] == winner:
                if not draw:
                    data[1] = data[1] + 1
                else:
                    data[3] = data[3] + 1
                details.seek(pos)
                pickle.dump(data, details)
            elif data[0] == loser:
                if not draw:
                    data[2] = data[2] + 1
                else:
                    data[3] = data[3] + 1
                details.seek(pos)
                pickle.dump(data, details)
            else:
                continue
        except EOFError:
            break
    details.close()
    return


# Users
def get_players():
    with open("./files/players.dat", 'rb') as players:
        data = pickle.load(players)
        user_1 = data['red']
        user_2 = data['yellow']
    return user_1, user_2
