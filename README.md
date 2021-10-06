Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 2: Edit distance
---
### _Exercise 1 - Levenshtein Distance_
Compute the minimal Levenshtein edit distance for the following pairs of sequences.

**a)** S1= "", S2= ""

**b)** S1= "A", S2= ""

**c)** S1= "AGATATA", S2= "TATATATA"

**d)** S1= "AGTCCT", S2= "CGCTCA"

**e)** S1= "TGCATAT", S2= "ATCCGAT"

**f)** S1= "ATCCGAT", S2= "TGCATAT"


### _Exercise 2 - Metric function_
Check if the corresponding functions are metric.

- [ ] TODO image

- [ ] TODO image

- [ ] TODO image

- [ ] TODO image


### _Exercise 3 - Programming assignment: Levenshtein Distance_

**a)** Implement the function levenshtein_substitution which takes two sequences of the same length and computes the minimum number of substitutions to transform one into another.


**b)** Implement the function levenshtein_deletion which takes two sequences of different length and returns the positions of characters from the longest sequences which should be deleted to transform the sequence into the other one. If such deletion can not be done the function should return None
