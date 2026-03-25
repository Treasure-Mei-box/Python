#Movie Catalog Manager
movies = [("Inception","Sci-Fi","2010"),("Titanic","Romance","1997"),("The Matrix","Sci-Fi","1999")]

while True:
    print("-------- Movie Catalog Menu -------")
    print("1. View all movies")
    print("2. Add new Movie.")
    print("3. Search by Title.")
    print("4. Exit.")
    
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        if not movies:
            print("No movies in catalog.")
        else:
            print("\n-------- Movie List --------")
            for i, movie in enumerate(movies,1):
                print(f"{i}.{movie[0]} | {movie[1]} | {movie[2]}")
    elif choice == "2":
        title = input("Enter movie title: ")
        genre = input("Enter movie Genre: ")
        year = input("Enter released year: ")
        movie_data = (title,genre,year)
        movies.append(movie_data)
        print("Movie added sucessfully.")
    elif choice == "3":
        search_title = input("Enter movie title to search: ")
        found = False
        for movie in movies:
            if movie[0].lower() == search_title.lower():
                print(f"Found: Title: {movie[0]}, Genre: {movie[1]}, Released Year: {movie[2]}")
                found = True
        if not found:
            print("Movie not found.")
            break
    elif choice == "4":
        print("Thank you for using the service.")
        break
    else:
        print("Invalid input. Try Again.")