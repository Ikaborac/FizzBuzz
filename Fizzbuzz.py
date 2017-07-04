unos=int(raw_input("Unesi broj izmedu 1 i 100:"))
for unos in range(1,unos+1):
    if unos%15==0:
        print "FizzBuzz"
    elif unos%5==0:
        print "Buzz"
    elif unos%3==0:
        print "Fizz"
    else:
        print unos




