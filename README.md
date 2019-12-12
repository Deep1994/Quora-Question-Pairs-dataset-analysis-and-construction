# Quora-Question-Pair-dataset-analysis-and-construction
This repository contains some analysis about the [Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs) dataset, also how to construct train/dev/test set accoring to the raw official released dataset.

The raw official released QQP dataset contains total 404301 pairs of questions on Quora. Systems must identify whether one question is a duplicate of the other. Models are evaluated based on accuracy.

I did some analysis about the dataset, and found some typos.

 |   | total number | paraphrases | none-paraphrases  
-|-|-|-|
Raw dataset | 404301 | 149263 | 255038

The number of paraphrases is correct, but the number of none-paraphrases is wrong. There are 11 pairs have wrong data format that do not split correctly witht "\t", all the wrong pairs ids are as follws:

2332	
12330
65477	
174372	
196865
198200	
227767	
264607	
282584	
283933	
364931

All of these pairs are none-paraphrases. After correct them, we accutually have 404301 - 11 = 404290 pairs of questions.

 |   | total number | paraphrases | none-paraphrases  
-|-|-|-|
Corrected dataset | 404290 | 149263 | 255027

## File description

+ data_analysis.py

Do the analysis and correct the raw dataset.

+ data_preprocess.py

Some preprocess for QQP dataset.

+ dataset.py

Get the train/dev/test set according to the raw dataset. Rondom 5000 paraphrases and 5000 none-paraphrases for dev, same as the test set, so dev set and test set contain 10000 pairs of questions, respectively. All the rest are considered as the train set.

 |   | total number | train | dev | test  
-|-|-|-|-|
Splited dataset | 404290 | 384290 | 10000 | 10000