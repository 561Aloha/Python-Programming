import csv

def read_csv(file_path, skip_header=True):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)
        for row in reader:
            data.append(row)
    return data

def display_top_collaborations():
    # Read CSV files
    top_rated_data = read_csv('imdb-top-rated.csv')
    top_casts_data = read_csv('imdb-top-casts.csv')

    # Extract titles from top-rated movies
    top_rated_titles = set(movie[1] for movie in top_rated_data)

    # Initialize dictionary to store collaborations
    collaborations = {}

    # Iterate through top-casts data and find collaborations
    for movie in top_casts_data:
        title = movie[0]
        if title in top_rated_titles:
            director = movie[2]
            actors = movie[3:]
            for actor in actors:
                if actor:
                    key = (director, actor)
                    collaborations[key] = collaborations.get(key, 0) + 1

    # Sort collaborations by the number of movies worked together in descending order
    sorted_collaborations = sorted(collaborations.items(), key=lambda x: x[1], reverse=True)

    # Display the ranking of collaborations
    print("Ranking of Collaborations:")
    for i, (key, num_movies) in enumerate(sorted_collaborations, start=1):
        if i >10:
            break #this is for only showing the first 10 results.
        if isinstance(key, tuple):  # Check if the key is a tuple
            director, actor = key
            print(f"{i}. Director: {director}, Actor: {actor}, Number of Movies: {num_movies}")
        else:
            print(f"{i}. Director/Actor: {key}, Number of Movies: {num_movies}")

def find_top_actors(top_grossing_path, top_casts_path):
    # Read CSV files
    top_grossing_data = read_csv(top_grossing_path)
    top_casts_data = read_csv(top_casts_path)

    # Extract movie titles from both datasets
    top_grossing_titles = set(movie[1] for movie in top_grossing_data)
    top_casts_titles = set(movie[0] for movie in top_casts_data)

    # Find common movie titles
    common_titles = top_grossing_titles.intersection(top_casts_titles)

    # Initialize dictionary to store actor rankings
    actor_rankings = {}

    # Iterate through common movie titles and extract actors from top-casts data
    for movie in top_casts_data:
        title = movie[0]
        if title in common_titles:
            actors = movie[3:]  # Assuming actors start from index 3
            for actor in actors:
                if actor:
                    actor_rankings[actor] = actor_rankings.get(actor, 0) + 1

    # Sort actor rankings by the number of movies worked in descending order
    sorted_actor_rankings = sorted(actor_rankings.items(), key=lambda x: x[1], reverse=True)

    # Display the ranking of actors
    print("Ranking of Actors in Top-Grossing Movies:")
    for i, (actor, num_movies) in enumerate(sorted_actor_rankings, start=1):
        if i > 10:
            break  # Show only the top 10 results
        print(f"{i}. Actor: {actor}, Number of Top-Grossing Movies: {num_movies}")



def main():
    display_top_collaborations()
    print()
    print()
    find_top_actors('imdb-top-grossing.csv', 'imdb-top-casts.csv')

if __name__ == "__main__":
    main()