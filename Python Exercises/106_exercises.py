# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for
# children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.


movie_rating = input("what is the movie rating ").strip().lower()

if movie_rating == '12':
    print("not suitable for under 12's")
elif movie_rating == '15':
    print("not suitable for under 15's")
elif movie_rating == '18':
    print("not suitable for under 18")
elif movie_rating == 'pg':
    print("general viewing but some scenes may be unsuitable for young children")
elif movie_rating == 'universal' or 'u':
    print("everyone can watch")
else:
    print("That is not a valid movie rating! Please try again")
