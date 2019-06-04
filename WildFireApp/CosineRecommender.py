
# Function that takes in project descriptions as input and outputs most similar projects
def get_recommendations(title, cosine_sim, indices):
    '''This function to create a content-based recommender. It will compute cosine similarity
    between all documents and return the top ten nearest documents in cosine similarity based
    off of description content.'''

    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    proj_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    projects = indices[indices[proj_indices]][:10]

    return projects
