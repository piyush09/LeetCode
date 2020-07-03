"""
ALgo: First sort the list of people, in the order of descending height. If multiple people are of the same height, sort them in ascending order of the number of people in front of them.
It gives correct position relative to people with equal and larger height.

When later, people are inserted with equal or smaller height, it will not affect this relative position.

T.C. - O(N^2) - Loop over people and sort in decreasing order of 'h' and increasing 'k' value.
        Insertion is O(N) operation.

S.C. - O(N)- Storing all the elements in the result list.
"""
def reconstructQueue(people):
    # First sort the list of people, in the order of descending height.
    # If multiple people are of the same height, sort them in ascending order of the number of people in front of them.
    people = sorted(people, key = lambda x: (-x[0], x[1]))

    res = []

    for p in people:
        # Inserting element p at index p[1]
        res.insert(p[1], p)
    return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print (reconstructQueue(people))