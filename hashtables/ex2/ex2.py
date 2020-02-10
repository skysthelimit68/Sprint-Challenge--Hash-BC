#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    for ticket in tickets:
        # key value pair : key => source, destination => destination
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.source is "NONE":
            route[0] = ticket.destination

    for i in range(1, len(route)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
        print(route[i])
    
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3)

print(result)