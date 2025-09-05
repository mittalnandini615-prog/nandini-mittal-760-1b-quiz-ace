# Initial Library
library = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'title': '1984', 'author': 'George Orwell'}
]

# Function to add a book 
def add_book(): 
    title = input("Enter book title: ") 
    author = input("Enter author: ") 
    book = {'title': title, 'author': author} 
    library.append(book) 
    print("Book added successfully!") 

# Function to search for a book by title 
def search_book(): 
    search_title = input("Enter the title to search: ").lower() 
    for book in library: 
        if book['title'].lower() == search_title: 
            print(f"Found: {book['title']} by {book['author']}") 
            return
    print("Book not found.") 

# Function to show all books 
def show_books(): 
    if not library: 
        print("No books in the library.") 
    else: 
        print("All books in the library:") 
        for book in library: 
            print(f"- {book['title']} by {book['author']}") 

# Main menu loop 
while True: 
    print("\nLibrary Management") 
    print("1. Add Book") 
    print("2. Search Book by Title") 
    print("3. Show All Books") 
    print("4. Exit") 
    choice = input("Choose an option (1-4): ") 
    if choice == '1': 
        add_book() 
    elif choice == '2': 
        search_book() 
    elif choice == '3': 
        show_books() 
    elif choice == '4': 
        print("Goodbye!") 
        break 
    else: 
        print("Invalid choice. Please try again.") 
