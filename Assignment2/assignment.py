# Part 1

# Read lines from CSV file
with open("assignment2_file.csv", "r") as f:
  lines = f.readlines()

# Create data structures by splitting the lines by comma
array1 = lines[0].strip().split(",")
tuple1 = tuple(lines[1].strip().split(","))
list1 = lines[2].strip().split(",")
set1 = set(lines[3].strip().split(","))

# Get keys and values of the dictionary
keys = tuple(lines[4].strip().split(","))
values = tuple(lines[5].strip().split(","))
# Create the dictionary
dictionary1 = dict(zip(keys, values))

# Display it
print(array1, tuple1, list1, set1, dictionary1)

# Create assignment2 file by opening it in write mode
with open("assignment2_file.txt", "w") as f:
  # Write all data structures + the new line character
  f.write(str(dictionary1) + "\n")
  f.write(str(set1) + "\n")
  f.write(str(list1) + "\n")
  f.write(str(tuple1) + "\n")
  f.write(str(array1) + "\n")

# Read the created file
with open("assignment2_file.txt", "r") as f:
  for line in f.readlines():
    # Print each line without the newline character
    print(line.strip())

# Checks
if "Fujairah" in list1:
  print("Fujairah found")
else:
  print(None)

if "brown" in set1:
  print("brown found")
else:
  print(None)

if "Data Science" in dictionary1.values():
  print("Data Science found in dictionary values")
else:
  print(None)


# Part 2
from sorts import insertionSort, mergeSort, quick_sort

# Sort the data structures
insertionSort(array1)
# Convert the tuple to a list and then back to a tuple (tuples are immutable)
tuple1 = list(tuple1)
mergeSort(tuple1)
tuple1 = tuple(tuple1)

quick_sort(list1, 0, len(list1)-1)

# Convert the set into a list and then back to a set (they don't support indexing)
set1 = list(set1)
quick_sort(set1, 0, len(set1)-1)
set1 = set(set1)
# Sort the dictionary by its values using a lambda function
dictionary1 = dict(sorted(dictionary1.items(), key=lambda x: x[1]))

# Write all sorted data structures + the new line character to the existing file by opening it in append mode
with open("assignment2_file.txt", "a") as f:
  f.write(str(dictionary1) + "\n")
  f.write(str(set1) + "\n")
  f.write(str(list1) + "\n")
  f.write(str(tuple1) + "\n")
  f.write(str(array1) + "\n")

with open("assignment2_file.txt", "r") as f:
  # Print all the lines
  for line in f.readlines():
    print(line.strip())

# Part 3

# Write everything to the CSV file
with open("assignment2_file.csv", "w") as f:
  f.write(str(dictionary1) + "\n")
  f.write(str(set1) + "\n")
  f.write(str(list1) + "\n")
  f.write(str(tuple1) + "\n")
  f.write(str(array1) + "\n")