from tabulate import tabulate
from colorama import Fore, init
import webbrowser

init(autoreset=True)

# -------------------- Welcome Section --------------------
print("Welcome to mystore".center(90, '-'))
user = input("Can you Enter your name:> ")
print(f"\nWelcome, {user} 😊 to our store!")

# -------------------- HTML Generation --------------------
html_content = f"""<html>
  <head><title>Thanks for shopping</title></head>
  <body>
    <h1>Thank you for shopping, {user}! 🛍️</h1>
  </body>
</html>
"""

with open("my_page.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# -------------------- Product Selection --------------------
print("\nWhich type of product do you want to purchase?")
print("1. Mobile\n2. Laptop\n3. Computer\n4. Tablet\n5. Watch")
a = int(input("Enter your choice:> "))

# -------------------- Main Product Match --------------------
match a:
    case 1:  # Mobile Section
        print("You chose Mobile\nChoose a brand:")
        print("1. Apple\n2. Samsung\n3. OnePlus\n4. Tecno\n5. Redmi")
        b = int(input("Enter your choice:> "))

        match b:
            case 1:  # Apple iPhones
                print("You chose Apple Mobile\nChoose model:")
                print("""1. iPhone 6: ₹50000
                         2. iPhone 7: ₹55000
                         3. iPhone 8: ₹70000
                         4. iPhone 9: ₹80000
                         5. iPhone X: ₹85000
                         6. iPhone 11: ₹90000
                         7. iPhone 12: ₹100000
                         8. iPhone 13: ₹120000
                         9. iPhone 14: ₹150000
                         10. iPhone 15: ₹180000""")
                iphone = int(input("Enter your choice:> "))
                prices = {
                    1: 50000, 2: 55000, 3: 70000, 4: 80000, 5: 85000,
                    6: 90000, 7: 100000, 8: 120000, 9: 150000, 10: 180000
                }
                if iphone in prices:
                    print(f"You chose iPhone {iphone} price is ₹{prices[iphone]}")
                else:
                    print("Invalid iPhone model selected.")

            case 2:  # Samsung Mobiles
                print("You chose Samsung Mobile\nChoose model:")
                samsung_models = {
                    1: ("Galaxy S21", 70000),
                    2: ("Galaxy S20", 60000),
                    3: ("Galaxy Note 20", 80000),
                    4: ("Galaxy A52", 30000),
                    5: ("Galaxy M32", 15000),
                    6: ("Galaxy Z Fold 3", 180000),
                    7: ("Galaxy Z Flip 3", 100000),
                    8: ("Galaxy A72", 35000),
                    9: ("Galaxy S10", 50000),
                    10: ("Galaxy Note 10", 55000),
                }

                for k, v in samsung_models.items():
                    print(f"{k}. Samsung {v[0]}: ₹{v[1]}")

                choice = int(input("Enter your choice:> "))
                if choice in samsung_models:
                    model, price = samsung_models[choice]
                    print(f"You chose Samsung {model} price is ₹{price}")
                else:
                    print("Invalid Samsung model.")

            case _:
                print("That brand isn't implemented yet.")

    case 2:  # Laptop Section
        print("\nYou chose Laptop\nWhich company?")
        print("1. Asus\n2. MAC\n3. Lenovo\n4. HP\n5. Dell\n6. Samsung")
        laptop = int(input("Enter your choice:> "))

        match laptop:
            case 1:  # Asus Laptops
                asus_laptops = [
                    [1, "💻 Vivobook 14", "₹35,000"],
                    [2, "💻 Vivobook 15", "₹40,000"],
                    [3, "💻 Vivobook S14", "₹60,000"],
                    [4, "💻 Vivobook S15", "₹70,000"],
                    [5, "💻 Ultra K14", "₹45,000"],
                    [6, "💻 Pro 14X", "₹90,000"],
                    [7, "💻 Pro 15", "₹1,10,000"],
                    [8, "💻 Flip 14", "₹55,000"],
                    [9, "💻 Vivobook 16X", "₹85,000"],
                    [10, "💻 Slate OLED", "₹65,000"],
                    [11, "💻 Go 15", "₹30,000"],
                    [12, "💻 13 Slate", "₹25,000"],
                    [13, "💻 Pro 16X OLED", "₹1,50,000"],
                    [14, "💻 S14 OLED", "₹1,30,000"],
                    [15, "💻 S15 OLED", "₹1,45,000"],
                    [16, "💻 Pro 17", "₹1,80,000"]
                ]

                print(Fore.GREEN + "\n🧾 Available Asus Vivobook models:")
                print(Fore.CYAN + tabulate(asus_laptops, headers=["No.", "Model", "Price"], tablefmt="fancy_grid"))

                selected = int(input(Fore.YELLOW + "Which model would you like to purchase? (Enter number):> "))
                if 1 <= selected <= len(asus_laptops):
                    model = asus_laptops[selected - 1]
                    print(Fore.GREEN + f"You chose {model[1]} priced at {model[2]}")
                else:
                    print(Fore.RED + "Invalid model selected.")

            case _:
                print("This laptop brand is not implemented yet.")

    case 3:
        print("You chose Computer.")
    case 4:
        print("You chose Tablet.")
    case 5:
        print("You chose Watch.")
    case _:
        print("Invalid product type choice 😒.")

# -------------------- Payment --------------------
if 1 <= a <= 5:
    pay = int(input("\nTo proceed with payment, enter 1. To exit, enter 0:> "))
    if pay == 1:
        print(Fore.GREEN + "✅ Payment successful! Thank you for shopping 😊")
        print(Fore.GREEN + f"You chose {model} priced at {price}")
        

    elif pay == 0:
        print("Okay, no problem. Visit again soon 😊")
    else:
        print("Invalid payment option 😒")

# -------------------- HTML Page Open --------------------
webbrowser.open("my_page.html")
