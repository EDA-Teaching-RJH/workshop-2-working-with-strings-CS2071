def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    print(pounds, percent)
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def pounds_to_float(d):
    d = float(d)
    # Neither of these def's return a value
    # why

def percent_to_float(p):
    p = float(p)*0.01

main()
