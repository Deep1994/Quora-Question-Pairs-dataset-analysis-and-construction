# Quora-Question-Pair-dataset-analysis-and-construction
This repository contains some analysis about the [Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs) dataset, also how to construct train/dev/test set accoring to the raw official released dataset.

The raw official released QQP dataset contains total 404301 pairs of questions on Quora. Systems must identify whether one question is a duplicate of the other. Models are evaluated based on accuracy.

I did some analysis about the dataset, and found some typos.

 |   | total number | paraphrases | none-paraphrases  
-|-|-|-|
raw dataset | 404301 | 149263 | 255038

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


