from collections import deque

graph =graph = {
    'YOU': ['Alice', 'Bob', 'Martin'],
    'Alice': ['Bob', 'Marti Sales Mango'],
    'Bob': [],  
    'Martin': [],
    'Marti Sales Mango': [],  
    'Jonny': []  
}

def person_is_seller(person):
    return 'Sales Mango' in person

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('No mango sellers found')
    return False

search('YOU')
