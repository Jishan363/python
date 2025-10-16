def factorial(n):
    if n<0:
        return "factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=5
print("factorial of",num,"is :",factorial(num))


Note: Please add the Python Selenium Automation Testing in TuteDude
