# 1. the first bug I spotted in exercise 5 was the error in the loop with no trailing colon. I found it from the traceback and then understood it better after consulting AI. This tells me that my debugging instincts are decent, but not solid enough to fully understand the issue to explain it myself.
# 2. apply_discount(price, tier) function works by checking the tier and applying the corresponding discount to the price. It's inputs are the OG price and the tier and it returns the discounted price. A colleague can use it without reading the body of the function because the parameters and return values are clear.
# 3. Google Gemini was used to help me understand the 3 errors in broken_sales.py. It only explained the errors from the traceback and helped me further my thinking on how to fix the errors. The use of AI helped build my understanding of the errors, and why each line of code was missing a vital piece of syntax. It did not give me the answers nor find a shortcut to fix the code. 



# exercise 1

# defining a function
def calculate_tax(price, rate):
    return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# exercise 2

# definining a function w/ multiple parameters

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# calling the function w/ diff tiers

original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")
    
# exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# calling the final_price function

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders: 
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# exercise 5
# use chat gpt to fix broken sales and in own words explain what is wrong and why the fix works

# exercise 6

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)

