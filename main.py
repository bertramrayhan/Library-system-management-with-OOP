class Book:
  def __init__(self, title : str, author : str, publication_year : int):
    self.title = title
    self.author = author
    self.publication_year = publication_year

  def get_info(self):
    return f'Title : {self.title}, Auther : {self.author}, Publication Year : {self.publication_year}'


class Library:
  def __init__(self):
    self.books = {}
  
  def add_book(self, book):
    self.books[book.title] = (book, True) # True if available and False if not available
    
  '''
  nanti bentuknya jadi :
  judul : (object buku, availability)
  '''
  
  def _find_book(self, title):
    if title in self.books:
      return self.books[title]
    return None, None
  
  def borrow_book(self, title):
    book, available = self._find_book(title)
    if book and available:
      self.books[title] = (book, False)
      return f'"{title}" is borrow by you'
    else:
      return f'"{title}" is not available'

  def return_book(self,title):
    book, available = self._find_book(title)
    if book:
      if not available:
        self.books[title] = (book, True)
        return f'You have return "{title}"'
      else:
        return f'"{title}" has not been borrowed'
    return f'"{title}" is not available'

  def availability(self, title):
    book, available = self._find_book(title)
    if available:
      return f'"{title}" is available'
    else:
      return f'"{title}" is not available'

  def info_books(self):
    counter = 1
    for book, available in self.books.values():
      print(f'{counter}.')
      print(f'Title : {book.title}\nAuthor : {book.author}\nPublication year : {book.publication_year}')
      counter += 1

  def info_book(self, title):
    book, available = self._find_book(title)
    if book:
      return f'Ttile : {book.title}\nAuthor : {book.author}\nPublication year : {book.publication_year}' 
    return f'"{title}" is not in here'

library = Library()

def borrow_book():
  user_input = input('What book do you want to borrow? ')
  return library.borrow_book(user_input)

def return_book():
  user_input = input('WHat book do you want to return? ')
  return library.return_book(user_input)

def availability():
  user_input = input('What book do you want to check? ')
  return library.availability(user_input)

def info_book():
  user_input = input('What book do you want to know? ')
  return library.info_book(user_input)

def for_developer():
  global library
  while True:
    title = input('what title book would you add? ')
    if title == 'exit':
      break
    else:
      author = input('Who is the author? ')
      while True:
        try:
          publication_year = int(input('when is the book publish? '))
          if not 1000 < publication_year <= 2100:
            raise Exception
        except:
          print('This is not a year')
          continue
        else:
          break
          
    book = Book(title, author, publication_year)
    library.add_book(book)

    print('The book has been added to the library')
    print()

def choices():
  print('Options : ')
  print('-------------------------------------------------------')
  print('1. Borrow book')
  print('2. Return book')
  print('3. Checking availability of book')
  print('4. see all of the books')
  print('5. Checking information of book')
  print('6. Exit')
  print('-------------------------------------------------------')

def checking_user_input():
  global switch
  user_input = input()
  if user_input == 'developer':
    for_developer()
  elif user_input == '1':
    print(borrow_book())
  elif user_input == '2':
    print(return_book())
  elif user_input == '3':
    print(availability())
  elif user_input == '4':
    library.info_books()
  elif user_input == '5':
    print(info_book())
  elif user_input == '6':
    switch = False
  else:
    print('This is not an option')

switch = True
def main():
  global switch
  print('Welcome to the library')
  print('How can i help you?')

  
  while switch:
    choices()
    checking_user_input()



book1 = Book('Hello', 'me', 2024)
library.add_book(book1)
book2 = Book('Nice', 'you', 2000)
library.add_book(book2)

if __name__ == '__main__':
  main()