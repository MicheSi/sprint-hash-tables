#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source # starting location
        self.destination = destination # where flight is going to


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {}
    route = []

    # loop through length of list, create key & value for each ticket
    for i in range(length):
        key = tickets[i].source
        value = tickets[i].destination

        flights[key] = value # this creates the key/value pair in the dict

    # if key is NONE, flight is start of route
    key = flights['NONE']

    # if value of key is not NONE, add flights to route
    while key != 'NONE':
        route.append(key)

        # set key to new destination
        key = flights[key]

    # value of key is NONE, it's the last destination
    route.append(key)

    return route
