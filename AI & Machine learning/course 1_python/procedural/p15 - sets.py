# ---- set = collection which is unordered, unindexed, and no duplicate elements
# ---- can also do set operations like union, intersection, difference, etc.
# unordered means we cannot access items using index or do slicing

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup' ,'fork'}

utensils.add('plate')
utensils.remove('fork')
utensils.update(dishes) # add all items from dishes to utensils

print(dishes.intersection(utensils)) # intersection of two sets
for x in utensils:
    print(x)

