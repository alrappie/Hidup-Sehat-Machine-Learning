# Recommendation
* The recommendation model is in recmmendation.py
* The dataset is in dataset folder 

## How to run the model
Here's a step-by-step command for run the model.

```py
from recommendation import Recommendation
person = Recommendation(DATASET_LOCATION.json,USER_INPUT)
person.recomendations()
```
* Example output if user input "saya ingin menjaga kesehatan mental saya lebih baik lagi"
![](sample_recommendation.png)