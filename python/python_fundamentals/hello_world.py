first_name = "Zen"
last_name = "Coder"
age = 27

print(first_name.lower())
# 1
print("Hello World")

# 2
name = "John"
print("Hello", name)
print("Hello " + name)

# 3
name = 42
print("Hello", name)
print("Hello " + str(name))

# 4
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love {} and {}".format(fave_food1, fave_food2))
print(f"I love {fave_food1} and {fave_food2}.")


for x in range(0, 10, 1):
    if x % 2 == 0:
    print(x)
