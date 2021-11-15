# `matplotlib` design patterns

It's easy to write messy `matplotlib` code, so I'm collecting examples of good/bad patterns and how to keep your code clean and usable. 

## Case studies:
- https://www.labri.fr/perso/nrougier/scientific-visualization.html
- https://github.com/sadielbartholomew/creative-matplotlib 

## General principles:
- separate out plotting and generation logic (i.e. don't have any loops or if statements with calls to `ax.plot` in them) 
- always use the OO API 
- follow a common layout 

## Anatomy of a plotting script 

1. Generate your data
2. Create a figure / axes
3. Format the axes
4. Plot the data
5. Perform any post-plot formatting 
6. Save the results

You should have one function that corresponds to each of these steps. Notice that data generation comes before the plotting happens - try to keep the data handling as far away from the plotting as possible.
