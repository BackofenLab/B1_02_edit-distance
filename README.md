Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
##### Exercise sheet 2: Edit operations and alignments
---




### _Programming assignment: Levenshtein Distance_

**a)** Implement the function **levenshtein_substitution()** which takes two sequences of the same length and 
computes the minimum number of substitutions to transform one into another.

**b)** Implement the function **levenshtein_deletion()** which takes two sequences of 
different length and returns the positions of characters from the longest sequences which should be deleted to 
transform the sequence into the other one.This should be returned as a list of indices (int).
If such deletion can not be done the function should return *None*. Also, if there are no editing operations needed return an empty list.

---

#### Recommended good practices

Here we have included some best practices helping you solve the exercises as efficiently as possible. First, clone the assignment repository.
    

```
$ git clone git@github.com:Bioinformatics-teaching/lecture-2-sequence-alignment-userID.git
```

Do not forget to use your own user ID. Now, answers the questions.


```
$ cd lecture-2-sequence-alignment-userID
$ emacs -nw exercise_sheet2.py
```

Include the changes and make a commit describing the modifications.


```
$ git add exercise_sheet2.py
$ git commit -m "Description of your modifications"
```

 
Send your results.       


```
$ git push
```

Done! But, it would be nice to know something about the score, wouldn't it? Let's check the autograding results. This PR will also be used by the teachers to include specific comments.


<img src="./figures/sheet2_classroom.gif" alt="Autograding" width=100%/>
