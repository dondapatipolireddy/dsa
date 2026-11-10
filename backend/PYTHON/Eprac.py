try:
    a=int(input("Enter the numerator: "))
    b=int(input("Enter the denominator: "))
    c=a//b
    print(c+"")
except ZeroDivisionError as e:
    print("{Error}:","divisor is zero")
except TypeError as e:
    print("{Error}:"," YOU ARE ASSIGNED UNSUPOORTED TO OBJECT")
except ValueError as e:
    print("{Error}:","your are provided different datatype")
except NameError as e:
    print("{Error}:","The value is undefined")
else:
    print("Division successful")
finally:
    print("Division operation completed")
