favorite_movies = [
    'X-Men: First Class',
    'X-Men: Days of Future Past',
    'Avengers: Infinity War',
    'Incredibles',
    'Mean Girls'
]

print("The list " + "favorite_movies" + " includes my top " + str(len(favorite_movies)) + " favorite movies")
print("This is my complete list of favorite movies: " + str(favorite_movies)) #print complete list

print("This is my list sorted alphabetically: " + str(sorted(favorite_movies))) #sorted list
print("This is my list without any sorting: " + str(favorite_movies)) #without sort
#Comparing the 2 statements, I notice sorted sorts them alphabetically. Just printing the statement without sorting leaves it sorted as it was typed in the initial list above.

favorite_movies.sort()
print(favorite_movies)
#I am noticing that when I attempt to run the entire script, I do not receive input for the last print statement. I looked it up, and it seems this is because the print statement I am trying to use is not refering to the sort that happened just before.
#If I remove the favorite_movies.sort() statement, the following print statement runs as expected.

favorite_movies.append('Finding Nemo')
print("This is my updated list of favorite movies with a 6th addition. They are as follows: " + str(sorted(favorite_movies)))