import json

path_book = 'database_book.json'

def load(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

def save(path, database):
    with open(path, 'w') as file:
        json.dump(database, file, indent=4)


def add(database, id, title, author, year):
    id = len(database)+1
    database[id] = {'title':title,
                  'author':author,
                  'year':year}


def delete(database, id):
    return


def edit():
    return


def book_list(base):
    for id, book in base.items():
        print(f"ID: {id}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    



database = load(path_book)
add(database, 1, 'Python dla bystrzakow', 'Nolan Illes', 2012)
book_list(database)
save(path_book, database)