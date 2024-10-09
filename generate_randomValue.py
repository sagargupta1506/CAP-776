# List of names to replace "StudentX"
names = [
"John", "Merry", "David", "Sophia", "Michael", "Emma", "James", "Olivia", "Robert", "Isabella",
"William", "Ava", "Richard", "Mia", "Joseph", "Amelia", "Charles", "Evelyn", "Thomas", "Abigail",
"Christopher", "Harper", "Daniel", "Emily", "Matthew", "Ella", "Anthony", "Elizabeth", "Mark", "Sofia",
"Donald", "Avery", "Paul", "Scarlett", "Steven", "Grace", "Andrew", "Chloe", "Kenneth", "Victoria",
"George", "Lily", "Joshua", "Aria", "Kevin", "Eleanor", "Brian", "Hannah", "Edward", "Lillian",
"Ronald", "Addison", "Timothy", "Aubrey", "Jason", "Ellie"
]   # Repeat to ensure we have enough names for 1000 students

# Input data as a string (replace this with reading from a file if needed)
data = """
Student1,1,Math:62,Science:86,English:41
Student2,2,Math:61,Science:54,English:99
Student3,3,Math:64,Science:67,English:65
Student4,4,Math:56,Science:92,English:49
Student5,5,Math:91,Science:50,English:82
Student6,6,Math:74,Science:50,English:99
Student7,7,Math:45,Science:80,English:84
Student8,8,Math:78,Science:78,English:98
Student9,9,Math:53,Science:63,English:41
Student10,10,Math:88,Science:79,English:87

"""  # Add the rest of your data

# Split the data into lines
lines = data.strip().split("\n")

# Replace student names with actual names
updated_records = []
for i, line in enumerate(lines):
    parts = line.split(",")
    if i < len(names):
        parts[0] = names[i]  # Replace "StudentX" with the corresponding name
    updated_records.append(",".join(parts))

# Output the updated records
updated_data = "\n".join(updated_records)

# Print or save the updated data
print(updated_data)
