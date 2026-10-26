# Module 10 Lab · Inventory List Manager
# Name: Fiona Harlan
# Reflection Questions:
# 1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
# I thought lists were going to be a lot more tedious and difficult to organize. Now, I know how to organize lists and find specific items within the list.
# 2. Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
# I used to work in gym sales, and when taking inventory we had to count everything and input it into a spreadsheet manually. With python, we can easily keep track of inventory and find specific items in alphabetical order, rather than redoing an entire spreadsheet everytime we had a shipment.

# EXERCISE 1 
print("--- Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# EXERCISE 2
print("--- Exercise 2: Index practice ---")
first_item = inventory[0]
last_item = inventory[-1]
middle_item = inventory[len(inventory) // 2]
print(first_item)
print(last_item)
print(middle_item)


# EXERCISE 3
print("--- Exercise 3: Slicing ---")
first_three = inventory[:3]
last_two = inventory[-2:]
every_other = inventory[::2]
print(first_three)
print(last_two)
print(every_other)


# EXERCISE 4
print("--- Exercise 4: Modify ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# EXERCISE 5 
print("--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught (tuples are immutable, which protects fixed coordinate data).")
    print(coords)


# EXERCISE 6 
print("--- Exercise 6: Average of a list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
avg = total / count
best_day = max(sales)
worst_day = min(sales)
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Best: {best_day}")
print(f"Worst: {worst_day}")


# EXERCISE 7
print("--- Exercise 7: Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.90, 2))
print(prices)
print(discounted)


# EXERCISE 8 
print("--- Exercise 8: Filter above threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)
high_sales_avg = sum(high_sales) / len(high_sales)
print(high_sales)
print(f"count: {len(high_sales)}")
print(f"avg: ~{high_sales_avg:.2f}")