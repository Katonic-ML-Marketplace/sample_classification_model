# Binary Classification Model

This repository contains the example and sample files to deploy a Binary Classification Model on Katonic Platform.

## Prerequisites for Deployment:


- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions.
 The first function helps to fetch the model. The second function is optional,if you are performing any kind of preprocessing on the data before prediction please add all the necessary steps into it and return the formatted input, else you can just return `False` if no processing is required. In the third function write down the code for prediction and return the results in the data structure supported by API response.   

- `schema.py`: Define your schema on how you should pass your input data in predict function.

- `requirements.txt`: Define the required packages along with specific versions this file.

## Sample Input Data for Prediction API

```python
{
    "data":[[1,3,0,0,5,0,0,0,0,0]]
}
```

## Sample Input Data for Feedback API

```python
{
  "predicted_label":[1,1,1,1,0,0,0,0,1,0,1,0],
  "true_label": [1,1,0,1,0,1,0,0,1,0,1,0]
}
```
