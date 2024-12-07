# Create a list, this is result
List_players = []
def convert_input(temp1):
    for i in temp1:
        name, score = i.split(' ')
        # Use method append to add to list
        List_players.append([name, int(score)])

def perform_operation(temp2):
    for i in temp2:
        # Split name, score to implement
        One_player= i.split(' ')
        if i.startswith("insert"):
            name, score = One_player[1], One_player[2]
            List_players.append([name, int(score)])
        elif i.startswith("remove"):
            name = One_player[1]
            for player in List_players:
                if player[0] == name:
                    List_players.remove(player)
                    break
        else:
            name, score = One_player[1], One_player[2]
            for player in List_players:
                if player[0] == name:
                    player[1] += int(score)
                    break


def sort_player():
    # Sorted follow the required in problem
    List_players.sort(key=lambda x: (-x[1], x[0]))

temp1 = list(map(str,input().split(', ')))
temp2 = list(map(str,input().split(', ')))


convert_input(temp1)
perform_operation(temp2)
sort_player()

for player in List_players:
    print(player[0],end=' ')

