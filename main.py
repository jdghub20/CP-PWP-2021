# Lets get max number froma list

#invoices = [6, 10, 20, 47, 69, 11, 50, 230, 20, 24, 39, 29, 45]


#def biggest(numbers):
#    biggest_number = invoices[0]
#    for number in invoices:
#        if number > biggest_number:
#            biggest_number = number
#    return biggest_number


#Print List

#print(biggest(invoices))

# movies is a list of tuples
#movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Follows", #8.0)("X-Men", 2)]

#print(type(movies))
#print(len(movies))
# ("Interstellar", 10)[0]  will print 'Interstellar'
# ("Interstellar", 10)[1]  will print 10

# Filter movies
#for movie in movies:
   # will print movies name
#   print(movie[0])  
   # will only print the rating
#   print(movie[1])

# create a function to see a movie specific to a rating
our_movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Follows", 8.0), ("X-Men", 2)]


def rating_filter(movies, max_rating):
  final_movies = []

  for movies in movies:
    if movies[1] >= max_rating:
      final_movies.append(movies[0])
  return final_movies    

print(rating_filter(our_movies, 1))