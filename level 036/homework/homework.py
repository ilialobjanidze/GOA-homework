# 1)The map() function applies a given function to all items in an iterable (like a list) and returns a new iterable
# 2)The filter() function is used to filter elements from an iterable based on a function that returns True or False


listn = [[98, 11, 29], [91, 2, 13], [18, 23, 192]]
average = list(map(lambda x: sum(x) / len(x), listn))
print(average)  



products = {
    'Chicken': True,
    'Mango': False,
    'Bread': True,
    'Soda': False
}

out_of_stock = dict(filter(lambda item: not item[1], products.items()))
print(out_of_stock) 

