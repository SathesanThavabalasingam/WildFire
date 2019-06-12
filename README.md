# [WildFire](https://insight-wildfire.appspot.com/)

<p align = "center">
<img src="./WildFireApp/static/img/logo.png">
</p>
<h4 align="center">Connecting vendors with the right buyers.</a></h4>


### What is WildFire?

Public institutions in Canada spend an estimated $22 billion dollars a year on the buying of goods and services from vendors. A critical problem is that buyers don't know which vendors to select for a given project. Part of this problem stems from the fact that vendors don't always know which projects to bid on. Therefore, the current system for the buying of goods and services in the public sector is inefficient due to:

(1) Projects being classified under predefined categories that are too general.

(2) Vendors not having any recommendations based on project content.  

Vendors need a better way to see the projects they bid on. A potential solution for this is to use Natural Language Processing to create a better content-based taxonomy for projects and to provide recommendations. 


### Using WildFire

Users can select to find a project and be presented with a unique project description. The model then provides keywords related to the project as well as a list of top recommender projects. Users can click each project for more information about the project. 

### How it Works

<p align = "center">
<img src="./WildFireApp/static/img/concept.png">
</p>

### Input and Preprocessing

Thousands of project descriptions are first preprocessed. The text information is preprocesed to remove a number of irrelevant features, such as special characters and stop words that do not convey import information with respect to the project content. The descriptions are then:

Tokenized: Given a character sequence and a defined document unit, tokenization is the task of chopping it up into pieces, called tokens 

Lemmatized:  Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma. For example, the lemmatized version of leaves is 'leaf'.

Vectorized: TF-IDF stands for “Term Frequency — Inverse Data Frequency”. First, we will learn what this term means mathematically.

Term Frequency (tf): gives us the frequency of the word in each document in the corpus. It is the ratio of number of times the word appears in a document compared to the total number of words in that document.

<p align = "center">
<img src="./WildFireApp/static/img/tf.png">
</p>

Inverse Data Frequency (idf): used to calculate the weight of rare words across all documents in the corpus. 

<p align="center">
<img src="./WildFireApp/static/img/idf.png">
</p>

Combining these two we come up with the TF-IDF score (w) for a word in a document in the corpus. It is the product of tf and idf:

<p align="center">
<img src="./WildFireApp/static/img/tfidf.png">
</p>

### Topic Modelling with Latent Dirichlecht Allocation

To create a structure that dynamically reflects specific project content, topic modelling can be used. Specifically, Latent Dirilect Allocation (LDA) is a NLP technique that can extract relevant topics from a corpus of documents in an unsupervised manner. Description of LDA 

<p align="center">
<img src="./WildFireApp/static/img/lda.png">
</p>

α is the per-document topic distributions,

β is the per-topic word distribution,

θ is the topic distribution for document m,

φ is the word distribution for topic k,

z is the topic for the n-th word in document m,

w is the specific word

In the plate model diagram above, you can see that w is grayed out. This is because it is the only observable variable in the system while the others are latent. Because of this, to tweak the model there are a few things you can mess with and below I focus on two.

α is a matrix where each row is a document and each column represents a topic. A value in row i and column j represents how likely document "m" contains topic "k". A symmetric distribution would mean that each topic is evenly distributed throughout the document while an asymmetric distribution favors certain topics over others. This affects the starting point of the model and can be used when you have a rough idea of how the topics are distributed to improve results.

β is a matrix where each row represents a topic and each column represents a word. A value in row i and column j represents how likely that topic "k" contains word "w". (How much a topic likes a word)

1. Each word that appears in the corpus is randomly assigned to one of the "k" topics. 
2. LDA iterates through each word "w" for each document "m" and tries to adjust the current topic – word assignment with a new assignment. 
3. A new topic “k” is assigned to word “w” with a probability which is a product of two probabilities p1 and p2. The first probability, p1 is based off of the proportion of words in document m that are assigned to a given topic. The second probability, p2 is based on the proportion of documents that contain word "w" for a given topic "k".
4. This entire process continues until no more advancements can be made in the probabilities assigned to each word in the corpus.

Taking a closer look at some of the visualized topics that have been extracted from the project discription, we can see that one of these topics is related to construction/renovation related content. Each topic is associated with a number of words as well as their probability of occurence within that designated topic.

![alt text](./WildFireApp/static/img/topic_vis_1.png)

Similarly, another topic conveys information related to projects describing medical/scientific equipment. 

![alt text](./WildFireApp/static/img/topic_vis_2.png)

The topics appear to be mapping on to real content that has been extracted from the project descriptions. However, we can take this a step further and ask ourselves if these topics are indeed valid. One way this can be determined is by looking at the categorical labels or each project description and identify the most frequent categories within each topic.

We can see below that for the "construction" topic, the most frequently occurring categorical label is "Building and facility maintenance and repair services". For the "medical/lab" topic, the most frequent categories are "Measuring and observing testing instruments" "Laboratory and scientific equipment" and "Medical diagnostic imaging and nuclear medicine products".

<p align="center">
<img src="./WildFireApp/static/img/topic_category.png">
</p>

### Content-Based Recommender System

The recommended projects are provided using cosine similarity. You use the cosine similarity score since it is independent of magnitude and is relatively easy and fast to calculate. Cosine similarity will identify the projects that are the most similar with respect to their content captured in their descriptions (since we are using the Tf-idf matrix).

<p align="center">
<img src="./WildFireApp/static/img/cosine_1.png">
</p>

a is the tf-idf weight for term i in the query.

b is the tf-idf weight for term i in the document.

The term weights in a document "b" affects the position of the document vector. 

An example target project (first row) and recommended project (second row) are provided below, along with their associated labels (second column). Notice that the recommended document has a label that is different from the target document. This is important, demonstrating that the recommender system can identify similar projects based on the description content that can identify projects from other categories that a user may not typically be exposed to.


| “The Hospital is seeking the professional services of a Consultant to conduct a review of Hospital Non Union Staff compensation and nomenclature. The Hospital wants to ensure...” |   Human resources services   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------:|
|        “Grand River Hospital (GRH) is requesting the professional services of a Consultant to conduct a review of Hospital Non Union Staff compensation and nomenclature...”       | Management advisory services |