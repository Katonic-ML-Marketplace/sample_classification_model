# Binary Classification Model

This repository contains the example and sample files to deploy a Binary Classification Model on Katonic Platform.

## Prerequisites for Deployment:


- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions.
 The first function helps to fetch the model. The second function is optional,if you are performing any kind of preprocessing on the data before prediction please add all the necessary steps into it and return the formatted input, else you can just return `False` if no processing is required. In the third function write down the code for prediction and return the results in the data structure supported by API response.   

 For more information on how to create and manage `launch.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,launch.py,-%2D%20This%20is%20the).

- `schema.py`: Define your schema on how you should pass your input data in predict function.

 For more information on how to create and manage `schema.py` you can visit [here](https://docs.katonic.ai/UserGuide/katonic-deploy/how-to-s/Deploy%20a%20Image%20Classification%20Model#:~:text=Copy-,schema.py,-%2D%20This%20file%20will).

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
