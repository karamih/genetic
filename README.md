# Genetic
Genetic algorithm for optimize two variables functions.<br>

*genetic.py* : the main file which include genetic algorithm.<br>
*ui.py* : gradio file for user interface.<br>
<hr>

## Test
for testing we use *cross in tray function* and try to optimize it.
<hr>
<img src='cross in tray.png'>

## Result
<img src='output.png'>
<hr>

## Params:
*function*: should enter a string that include just two variable that appear like X1 and X2.<br>

*start*: the start of X1 and X2 range.<br>

*end*: the end of X1 and X2 range.<br>

*n_first_population*: initial number of numbers.<br>

*n_cross_over_rate*: rate of cross over.<br>

*n_mutation_rate*: rate of mutation on cross over numbers.<br>

*iteration*: number of iteration to convex.<br>

*alpha*: alpha could be considered as a coefficient for cross over, between 0 to 1.<br>

*minima*: if *True* it find the minimum, if *False* it find the maximum.<br>
