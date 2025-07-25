import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp.center(50))
budget = int(input("Enter your budget:> "))
price = 1000    

# when the price is greater than the budget, we print a message
if budget < price:
    ans = price - budget
    print("\nYou can't afford this product. To buy this product, you need", ans, "more Rs...")
    print("\nThank you. Visit again!..")

# when the price is less than or equal to the budget
elif budget >= price:
    ans1 = budget - price
    print("\nThis product is within your budget.")
    print("After buying this, you'll still have", ans1, "Rs left.")
    p = int(input("\nEnter 1 for{containue} and 0 for{exit}:>"))
    
    if p == 0:
        print("👍 No problem.")
        print("Thank you. Visit again 😊")
    elif p == 1:    
        print("👍 Okay, let's continue.")
 
        quantity = int(input("\nHow many quantities do you want to buy?:> "))
        total = price * quantity

        print("This product has been added to your cart.".center(100))
        print(f"\nYour total bill is {total}".center(100))

        print("😊 Thank you for purchasing this product.".center(190))
        print("😀 Visit again!".center(190))
