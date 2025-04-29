print("URK24CS1182")
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 10,
    "apple": 0,
    "orange": 5,
    "pear": 8
}
for key in prices:
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key])
total = 0
for key in prices:
    value = prices[key] * stock[key]
    print(f"Revenue from {key}: {value}")
    total += value
print("Total revenue:", total)          