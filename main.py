class Book:
  def __init__(self, title, author, publication_year):
    self.title = title
    self.author = author
    self.publication_year = publication_year

  def get_info(self):
    return f'Title : {self.title}, Auther : {self.author}, Publication Year : {self.publication_year}'


class Library:
  def __init__(self):
    self.books = {}
  
  def add_book(self, book):
    self.books[book] = 'Available'

  def borrow_book(self, title):
    pass

library = Library()

def for_developer():
  global library
  while True:
    title = input('what title book would you add?')
    if title == 'exit':
      break
    else:
      author = input('Who is the author?')
      publication_year = input('when is the book publish?')

    book = Book(title, author, publication_year)
    library.add_book(book)

def choices():
  print('1. Borrow book')
  print('2. Return book')
  print('3. Checking availability of book')
  print('4. see all of the books')
  print('5. Exit')

def main():
  print('Welcome to the library')
  print('How can i help you?')

  switch = True
  
  while switch:
    choices()
    user_input = input()
    if user_input == 'developer':
      for_developer()




if __name__ == '__main__':
  main()