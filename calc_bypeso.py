import math

def calc_weight(discount, cps):
    '''
	Function to calculate discount weight.
	This function, receives a list of dictionaries with the key: 'weight' 
	indicating the weight you wish to discount from the object.

	It will be discounted more the object who has the largest weight.
        If all weights are equal, it will be discounted proportionally.

	Arguments:
	    discount {int} - How much do you want to discount?
	    cps {list} - list of dictionaries

	Return
	    {list}
    '''
    
    cp_calculate = [c for c in cps if c['weight'] > 0]
    if cp_calculate:
        discount_weight_sum = sum(c['weight'] for c in cp_calculate)

        rest = 0
        for c in cp_calculate:
            c['weight'] = math.floor(discount * c['weight'] / (discount_weight_sum)) # round for less

        discount_weight_sum = sum(c['weight'] for c in cp_calculate)
        rest = discount - discount_weight_sum
        if rest > 0:
	   # orders it by the largest number, then uses it to add up with the rest that is left, 
           # just once and already to the loop
            weights = sorted((c['weight'] for c in cp_calculate), reverse=True)
            for w in weights:
                for c in cp_calculate:
                    if w == c['weight']:
                        c['weight'] = c['weight'] + rest
                        break
                break

        return cp_calculate
    else:
        return cps

cps = [{'id': 5, 'weight': 10}, {'id': 6, 'weight': 10}, {'id': 3, 'weight': 5}, {'id': 2, 'weight': 0}]
calc_weight(20, cps)

'''
Result:
	[{'id': 5, 'discount_weight': 8},
	 {'id': 6, 'discount_weight': 8},
	 {'id': 3, 'discount_weight': 4}]
'''


