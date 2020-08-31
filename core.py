keywords = list()
try:
    while True:
        key = input("Please Enter Your Loved Keywords ( Cntrl + C To End ) :  ")
        keywords.append(key)
except KeyboardInterrupt:
    pass

print(keywords)