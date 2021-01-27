
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
# our_movies = [("Interstellar", 10), ("Ironman", 8.2), ("It Follows", 8.0), ("X-Men", 2)]


# def rating_filter(movies, max_rating):
#   final_movies = []

#   for movies in movies:
#     if movies[1] >= max_rating:
#       final_movies.append(movies[0])
#   return final_movies    

# print(rating_filter(our_movies, 1))

# learning about Dictionary

# phone_book = {"John": "444-222-4444", "Billy": "444-111-2222"}
# print(phone_book)

# movies = {"Shaw Shank Redemption": 9.7, "The God Father": 8.0}

# # Authors blogs stored in a variable

# authors = {"Rafeh Qazi": [ "b1", "cleverprogrammer.com/blog/2"], "Naz": [ "b1", "cleverprogrammer.com/blog/3"]}

# to print just b1 value of Naz
# print(authors["Naz"][0]) -- b1 associated with Key Naz
# print(authors["Rafeh"][1]) -- "cleverprogrammer.com/blog/2 associated with Key Rafeh

# Create a Wrod frequency counter
# In dictionary key are unique
# Info is not order
# List is good for maitain order

# final_answer = {"hey": 1, "Hey": 1, "what": 2, "are": 1, "you": 1, "doing": 1, "there": 1}

# sentence = "Hey what woop woop wop wop di dop dop there what are you doing"



# # for word in sentence.split():
# #   # if I am finding it for the first time, create a key with that word and set its value to 1

# #   # If I have already seen the word... Then increment its' value by 1

# #   if word not in final_dictionary:
# #       final_dictionary[word] = 1
# #   else:
# #       final_dictionary[word] = final_dictionary[word] + 1

# # print(final_dictionary)        

# def word_frequency(sentence):
#   final_dictionary ={}
#   for word in sentence.split():
#     if word not in final_dictionary:
#       final_dictionary[word] = 1
#   else:
#       final_dictionary[word] += 1
#   return final_dictionary 

# print(word_frequency(sentence))

# Things required fro the game
# board
# display board
# play game function
# check win
   # check rows
   # check columns
   # check diagnols
# check for tie


board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_",]

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
  
  # Display initial board
  display_board()

  handle_turn()

