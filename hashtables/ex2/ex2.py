#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {}
    route = []

    # create key & value for each ticket
    for i in range(length):
        key = tickets[i].source
        value = tickets[i].destination

        flights[key] = value

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
