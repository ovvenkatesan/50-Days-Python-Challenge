# NameList.py

# 1. Store 5 names in a list
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# 2. Print a header for the output
print("Names and their lengths:")
print("------------------------")

# 3. Loop through the list and print each name and its length
for name in names:
  length = len(name)
  print(f"Name: {name}, Length: {length}")
