from vars import path,task

import os
###
        # script that make a answer files for every user 
###

# Define the time stamps to be written to the time files
time_txt = ["20:15","20:20","20:26","20:40","20:46","22:00"]
# Define the number of test files to be executed
test_ver = int(input("who meny vertions of test answer you have? :"))
# Define the range of test versions
ver = [i+1 for i in range(test_ver)]
# Scan the users directory and retrieve the name of each user
users = os.scandir(path)
usernames = [user.name for user in users]

# Execute the following code for each test version
for i in ver:
    # Open the current test file
    with open(path+f"\\..\\{task}\\test{i}.py", "r") as f:
        # Store the contents of the file as a variable with a unique name
        exec(f'test_file_{i} = f.read()')

# Execute the following code for each user
for i in range(len(usernames)):
    # Retrieve the name of the current user
    user = usernames[i]
    # Determine the version of the test file to be used for the current user
    user_ver = i%len(ver) + 1
    # Determine the time stamp to be written to the time file for the current user
    time_ver = i%len(time_txt)
    # Define the path to the Python file to be written for the current user
    file_path = f"{path}\\{user}\\{task}.py"
    # Define the path to the time file to be written for the current user
    time_file_path = file_path[:-3]+"-time.txt"
    
    # Define the code to be executed to write the test file for the current user
    to_write = f'task_file.write(test_file_{user_ver})'
    
    try:
        # Write the test file for the current user
        with open(file_path, "w") as task_file:
                exec(to_write)
    except:
        score = "write error"
    
    try:
        # Write the time stamp to the time file for the current user
        with open(time_file_path, "w") as time_task_file:
                time_task_file.write(time_txt[time_ver])
    except:
        score = "write error"
