def main():
    slow = input("Input ")
    myFunction(slow)

def myFunction(text):
    newtxt = str(text).replace(" ", ".")
    print(newtxt)

main()
