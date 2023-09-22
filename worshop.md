# Workshop III

### 1. In your own words, describe what vector embeddings are and what they are useful for.

An embeddings vector is a tensor representation of text, image, or audio data 
that aims to capture the similarity of natural language.

### 2. What do you think is the best distance criterion to estimate how far two embeddings (vectors) are from each other? Why?

The best way to choose a distance criterion for a particular application is to 
experiment with different metrics and see which one performs best. 

* If the embeddings are dense and the relationships between the different 
dimensions are relatively simple, then Euclidean distance is often a good choice.

* If the embeddings are sparse or the relationships between the different 
dimensions are more complex, then Manhattan distance may be a better choice.

* If the embeddings are normalized and the relationships between the different 
dimensions are directional, then cosine distance may be a better choice.

* The nature of the data: Some distance criteria are better suited for certain 
types of data than others. For example, cosine distance is often a good choice 
for text data, while Euclidean distance is often a good choice for image data.

* Computational efficiency: Some distance criteria are more computationally 
efficient than others. This is important to consider if the distance 
criterion will be used in a large-scale application.

### 4. What do you think that could make these types of systems more robust in terms of semantics and functionality?

* Regularization.
* Using larger and more diverse datasets.
* Incorporating additional knowledge into the training process.
* Using more sophisticated training algorithms.
* Developing new evaluation metrics.