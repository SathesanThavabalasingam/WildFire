from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import CosineRecommender as recs


# Create the application object
app = Flask(__name__)

l
# create function to assign target text to topic label
def classify(model,data):
    # the dataset to predict on (first two samples were also in the training set so one can compare)
    # Vectorize the training set using the model features as vocabulary
    tf_vectorizer = CountVectorizer(vocabulary=X_text_c_full_feature_names)
    tf = tf_vectorizer.fit_transform(data)

    # transform method returns a matrix with one line per document, columns being topics weight
    predicted = model.transform(tf)
    return predicted


@app.route("/", methods=["POST","GET"])
def home_page():
	return render_template('index.html')

@app.route('/items', methods=["POST","GET"])
def uploaduj():

    val = indices.sample(1).index[0]
    # Filter lengths less than n
    if len(val) > 300:
        random_project = val
        recommended = recs.get_recommendations(random_project, cosine_sim, indices)
        preds = classify(lda_model_full, [random_project])
        pred = str(np.argmax(preds))
        accuracy = np.amax(preds)*100
        return render_template("index.html", var=random_project,
                               proj1=recommended.index[0],
                               proj2=recommended.index[1],
                               proj3=recommended.index[2],
                               proj4=recommended.index[3],
                               proj5=recommended.index[4],
                               proj6=recommended.index[5],
                               proj7=recommended.index[6],
                               proj8=recommended.index[7],
                               proj9=recommended.index[8],
                               proj10=recommended.index[9],
                               acc=accuracy,
                               topic="Topic_"+pred+".png")
    else:
        return render_template("index.html", var="Description not found. Please try again.", topic="404.png")

# End-point used to clear cache
@app.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8080) # to run on port 8080


# Save model and related elements for later usage in Web Application.
import pickle
with open('data.pickle', 'wb') as f:
    pickle.dump([indices,cosine_sim], f)
    f.close()