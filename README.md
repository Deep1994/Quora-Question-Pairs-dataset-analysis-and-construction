# Quora-Question-Pair-dataset-analysis-and-construction
This repository contains some analysis about the [Quora Question Pairs](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs) dataset, also how to construct train/dev/test set accoring to the raw official released dataset.

The raw official released QQP dataset contains total 404301 pairs of questions on Quora. Systems must identify whether one question is a duplicate of the other. Models are evaluated based on accuracy.

I did some analysis about the dataset, and found some typos.

 |   | total number | paraphrases | none-paraphrases  
-|-|-|-|
raw dataset | 404301 | 149263 | 255038

The number of paraphrases is correct, but the number of none-paraphrases is wrong. There are 11 pairs have wrong data format that do not split correctly witht "\t", all the wrong pairs is as follws:

2332	4637	4638	"Which is the best RO water purifier in Ahmedabad?
"	What is the best water purifier available in India?	0
12330	23766	23767	Why did Kaley Cuoco cut her hair? Is it for the BBT show or did she just want to?	"Is Kaley Cuoco doing her best in season 8? Any comments on her new look?
"	0
65477	113627	113628	Any idea of dresses for a special 15-year-old's party?	"Where can I find a dress I seen last night in a party? I took a picture of girl wearing that beautiful dress. I like it to grab into my closet. Any fashion forums that can help me to find this lovely dress?
"	0
174372	268758	268759	Why do people wear black on the day of Makar Sankranti?	"Why do Indians celebrate Makar Sankranti?
I would like Tamils to respond, if Tamil teachers did specifically teach them something in School."	0
196865	297681	297682	Mohammad Ali Jinnah was a mass murderer. How many of you support this?	"What kind of person was Muhammad Ali Jinnah? Why did joined Muslim league?
"	0
198200	99321	4637	Which is the best RO water purifier in Patna?	"Which is the best RO water purifier in Ahmedabad?
"	0
227767	336684	336685	"Is the book Who Is Muhammad? [Book] By Jafar Subhani (Author) the best ever book about prophet muhammad?
"	Was Muhammad a real historical figure? What is the evidence for his existence?	0
264607	381419	381420	"Given a set of busy time intervals of two people as in a calendar, what is the algorithmic approach to find the free time intervals of both the people so as to arrange a new meeting?
"	What is the algorithmic approach to find the free-time intervals of both people so they can arrange a meeting, given the set of busy-time intervals of two people, as in a calendar?	0
282584	216251	402550	What is the sum of all 4 digit numbers that can be formed by the digits 0, 1, 2, 3, 4? No repetitions allowed.	"How do I Simplify the following matrices: 
\1. -5 [-7 0 0 5]; 2. 3 [6 4 5 -5 3 1]?"	0
283933	404107	404108	"What does the Quran say about the Bible?
"	What does the Quran say about homosexuality?	0
364931	19408	402550	Mathematical Puzzles: What is () + () + () = 30 using 1,3,5,7,9,11,13,15?	"How do I Simplify the following matrices: 
\1. -5 [-7 0 0 5]; 2. 3 [6 4 5 -5 3 1]?"	0

