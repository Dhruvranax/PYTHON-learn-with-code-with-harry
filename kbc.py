import random
import webbrowser

# ----------- Welcome section -------------------
user = input("Enter your name: > ")
print(f"Welcome {user} to the KBC Game!\nWe hope you win the maximum prize!")

 

# -------------- Price Ladder -------------------
prices = {
    1: 10000, 2: 55000, 3: 90000, 4: 120000, 5: 500000,
    6: 1100000, 7: 2000000, 8: 2900000, 9: 4500000, 10: 7000000,
    11: 10000000, 12: 15000000, 13: 20000000, 14: 25000000, 15: 30000000
}
print("\nLet's start the game!\n")

# -------------- Questions Section -------------------
questions = [
    ("What is the capital of Australia?", {"A": "Sydney", "B": "Melbourne", "C": "Canberra", "D": "Perth"}, "C"),
    ("Which planet is known as the Red Planet?", {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"}, "B"),
    ("Who wrote the Indian national anthem?", {"A": "Bankim Chandra", "B": "Sarojini Naidu", "C": "Rabindranath Tagore", "D": "Subhash Chandra Bose"}, "C"),
    ("Which gas do plants absorb?", {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Hydrogen"}, "B"),
    ("First woman Prime Minister of India?", {"A": "Sonia Gandhi", "B": "Sarojini Naidu", "C": "Indira Gandhi", "D": "Pratibha Patil"}, "C"),
    ("Longest river in the world?", {"A": "Amazon", "B": "Yangtze", "C": "Mississippi", "D": "Nile"}, "D"),
    ("In which year did India gain independence?", {"A": "1942", "B": "1945", "C": "1947", "D": "1950"}, "C"),
    ("Who is the 'Missile Man of India'?", {"A": "Vikram Sarabhai", "B": "APJ Abdul Kalam", "C": "C.V. Raman", "D": "Homi Bhabha"}, "B"),
    ("What does 'I' in ISRO stand for?", {"A": "Indian", "B": "International", "C": "Institute", "D": "Innovation"}, "A"),
    ("State known as 'Land of Five Rivers'?", {"A": "Uttar Pradesh", "B": "Punjab", "C": "Haryana", "D": "Bihar"}, "B"),
    ("Who invented the light bulb?", {"A": "Alexander Graham Bell", "B": "Isaac Newton", "C": "Thomas Edison", "D": "Nikola Tesla"}, "C"),
    ("Which Mughal emperor built Taj Mahal?", {"A": "Akbar", "B": "Shah Jahan", "C": "Jahangir", "D": "Aurangzeb"}, "B"),
    ("Who is 'The Little Master' in cricket?", {"A": "Virat Kohli", "B": "Sunil Gavaskar", "C": "M.S. Dhoni", "D": "Kapil Dev"}, "B"),
    ("What is India's national animal?", {"A": "Lion", "B": "Tiger", "C": "Elephant", "D": "Leopard"}, "B"),
    ("Smallest unit of life?", {"A": "Tissue", "B": "Organ", "C": "Cell", "D": "Molecule"}, "C")
]

# -------------- Game Logic -------------------
used_questions = set()

for q_no in range(1, 16):
    print(f"\nQuestion {q_no} for ₹{prices[q_no]:,}...")

    # Get a random question not already asked
    while True:
        index = random.randint(0, len(questions) - 1)
        if index not in used_questions:
            used_questions.add(index)
            break

    question, options, correct = questions[index]

    # Print the question and options
    print(f"\n{question}")
    for key, val in options.items():
        print(f"{key}: {val}")

    # Get user input
    ans = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Check the answer
    if ans == correct:
        print(f"✅ Correct! You’ve won ₹{prices[q_no]:,}.\n")
    else:
        print(f"❌ Wrong answer! The correct answer was '{correct}: {options[correct]}'.")
        print(f"You leave with ₹{prices.get(q_no - 1, 0):,}.\n")
        break
else:
    print("🎉 Congratulations! You've won ₹3 Crore!!! 🎉")

html_content = f"""<html>
  <head><title>Thanks for playing</title>
  </head>
  <body style="background-color: coral;">
  <center>
    <h1 style="color: black;">Thank you for playing, {user}! 😊</h1>
    <h3 style="color: green;">{user} you win total  ₹{prices.get(q_no - 1, 0):,} </h3>
    </center>
  </body>
</html>
"""

with open("my_page.html", "w", encoding="utf-8") as f:
    f.write(html_content)


print(f"Thank you for playing, {user}! 🙌")
webbrowser.open("my_page.html")
