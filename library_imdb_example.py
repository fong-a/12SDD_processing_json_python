# easy mode - use a library that contains methods for easy access
# just read documentation https://github.com/itsmehemant7/PyMovieDb

from PyMovieDb import IMDB
imdb = IMDB()
res = imdb.get_by_name('Rick and Morty', tv=True)
print(res)

