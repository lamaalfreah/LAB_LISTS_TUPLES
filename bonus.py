movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


filtered_movies = []

for movie_title, rlease_year, ratings in movies:
    average = round(sum(ratings) / len(ratings), 2)
    if average >= 6.0:
        filtered_movies.append((movie_title, rlease_year, average))

n = len(filtered_movies)
for i in range(n):
    for j in range(0, n - i - 1):
        if filtered_movies[j][2] < filtered_movies[j + 1][2]:
            filtered_movies[j], filtered_movies[j + 1] = filtered_movies[j + 1], filtered_movies[j]

i:int =1
print("Movie Ratings Analysis:")
for (title, year, avg) in filtered_movies:
    print(f"{i}. {title} ({year}) - Average rating: {avg} ★")
    i+=1