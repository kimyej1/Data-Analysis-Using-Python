###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("ufo-sightings.csv")
from nose.tools import assert_equal

'''
1. Import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''

import csv
filepath = "ufo-sightings.csv"
ufosightings = []

# your code here
with open("ufo-sightings.csv", 'r') as ufofile:
    reader = csv.DictReader(ufofile)

    ufosightings = [row for row in reader]
    print(reader.fieldnames)

'''
2. How many sightings were there in total?  Put the count in "ufosightings_count" and print the result.
'''
# your code here
ufosightings_count = 0
for ufo in ufosightings:
    ufosightings_count += 1
print(ufosightings_count)

'''
3. How many sightings were there in the US?  Put the US sightings in "sightings_us" and print.

Hint: Check for ufo sightings where the country is 'us'.

'''

# your code here
sightings_us = [row for row in ufosightings if row["country"] == "us"]
print(sightings_us)

'''
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''

#First, define a Python function that checks if a given duration (seconds) is "valid"
def is_valid_duration(duration_as_string):
    # your code here
    try:
        seconds = float(duration_as_string)

    except ValueError:

        return False
    else:
        return seconds > 10

fball = [row for row in sightings_us if(is_valid_duration(row["duration (seconds)"]) and row["shape"] == "fireball")]
print(fball)

for f in fball:
    print(f["datetime"], f["state"])

'''
5. Sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''

# your code here
fballsorted = sorted(fball, key = lambda x : float(x["duration (seconds)"]), reverse=True)

'''
6. What state had the longest lasting "fireball"?   Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''

# your code here
state = max(fball, key = lambda x: float(x["duration (seconds)"]))["state"]
print(state)

'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
Write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings
Note: Consider all sightings stored in "ufosightings".

'''

# your code here
min_duration = float(min(ufosightings, key = lambda x: x["duration (seconds)"] )["duration (seconds)"])
print(min_duration)

'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

#Create a new list containing values from the "shape" column in ufosightings.
# your code here
sightings_shapes = [row["shape"] for row in ufosightings]

#Create a new dictionary with values of that column as keys and the counts as values.
# your code here
count = {}
for shape in sightings_shapes :
    if shape not in count:
        count[shape] = 0
    count[shape] = count[shape] + 1

#Get a list of the dictionary keys and values (use the items() method) and sort them in reverse order, from greatest (most sightings) to least.
#Get and print the top 3.
# your code here
<<<<<<< HEAD
=======

>>>>>>> origin/main
top3shapes = sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]
