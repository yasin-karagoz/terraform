def greeting(name, departmant):
    print("welcome, " + name)
    print("You are part of " + departmant)

greeting("kay")


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month,days):
    print(month + " has " + str(days) + " days.")
month_days("June","30")
month_days("July","31")


def f1(x, y):
    z = x*y  # the area is base*height
    print("The area is " + str(z))

def rectangle_area(base, height):
    z =base*height
    print("The area is " + str(z))
rectangle_area(5,6)