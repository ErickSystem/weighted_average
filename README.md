# WEIGHTED AVERAGE
## Calculation of weighted average, per data dictionary list
```python
    In [3]: cps = [{'id': 5, 'weight': 10}, {'id': 6, 'weight': 10}, {'id': 3, 'weight': 5}, {'id': 2, 'weight': 0}]  
    In [4]: calc_weight(20, cps)

    Out[4]: [{'id': 5, 'weight': 8},
             {'id': 6, 'weight': 8}, 
             {'id': 3, 'weight': 4}]

    In [5]: cps = [{'id': 5, 'weight': 10}, {'id': 6, 'weight': 10}, {'id': 3, 'weight': 10}, {'id': 2, 'weight': 10}]
    In [6]: calc_weight(30, cps)      

    Out[6]: 
    [{'id': 5, 'weight': 9},
    {'id': 6, 'weight': 7},
    {'id': 3, 'weight': 7},
    {'id': 2, 'weight': 7}]

    In [7]: cps = [{'id': 5, 'weight': 0}, {'id': 6, 'weight': 0}, {'id': 3, 'weight': 10}, {'id': 2, 'weight': 10}]  
    In [8]: calc_weight(30, cps)
                                                                                          
    Out[8]: [{'id': 3, 'weight': 15}, {'id': 2, 'weight': 15}]


```
