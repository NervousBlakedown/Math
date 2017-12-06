> runif(5, min = 43, max = 97)
[1] 83.50847 64.94296 52.10988 57.30297 57.39939
> sample(47:98, 23, TRUE)
 [1] 75 76 55 79 98 65 57 94 75 78 91 67 91 73 97 84 86 80 53 66 97 95 67
> test.scores <- sample(47:98, 23, TRUE)
> mean(test.scores)
[1] 70.47826
> mode(test.scores)
[1] "numeric"
> min(test.scores)
[1] 47
> max(test.scores)
[1] 98
