#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = []
    for items in tickets:
        if items not in cache:
            cache[items.source] = items.destination

    for items in tickets:
        if items.source == "NONE":
            route.append(items.destination)
    
    while route[-1] != "NONE":
        route.append(cache[route[-1]])

    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]
# reconstruct_trip(tickets, 3)