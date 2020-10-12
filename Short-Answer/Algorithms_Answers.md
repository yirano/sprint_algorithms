#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)` - This will take on the order of _n_ number of operations to complete. 


b) `O(n log n)` - This one almost tricked me but the `while` loop can quickly catch up dependent on the `j` value, meaning that whatever that value is can quickly shift the runtime of this algorithm. It's kind of like searching through a binary search tree.


c) `O(n)` - This will take on the order of _n_ number of operations to complete. 

## Exercise II

```
start at the middle floor of this n-story building:
    drop an egg and if it breaks:
        go down one floor
        broken += 0

    if it doesn't  break:
        go up one floor
        broken += 1
```

Runtime --> O(n)? You're just going up and down the stairs until you create an ocean of yolk.
