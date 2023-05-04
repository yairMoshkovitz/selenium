# This function tests the user submissions for a given task and calculates their scores.
def test(task,st_time):
    # Import necessary modules and variables
    from vars import path
    from tabulate import tabulate
    import os
    import pandas as pd

    # Define column names for the output dataframes
    time_col = "Time-"+ task
    score_col = "score-"+ task

    # Define empty dictionaries to store data for each user and for each task
    data ={ 'user' : [], task : []}
    task_data ={ 'user' : [], 'score' : [],'time':[] }

    # Try to read the test file to chack the subbmission code
    with open(path+f"\\..\\{task}\\test.py", "r") as f:
        test_file = f.read()

    # Get a list of all the user directories
    users = os.scandir(path)
    usernames = [user.name for user in users]

    

    # Loop through each user and test their submission for the given task
    for user in usernames:
        # Initialize difference_time to -1
        difference_time =  -1

        # Try to read the submission file and calculate score
        try:
            score = 0 
            file_path = f"{path}\\{user}\\{task}.py"
            time_file_path = file_path[:-3]+"-time.txt"

            # Try to read the time file and calculate time difference
            try:
                with open(time_file_path, "r") as time_file:
                        send_time = time_file.read()

                # Calculate time difference and deduct score for late submissions
                if int(send_time.split(":")[0]) == st_time[0] :
                    difference_time = int(send_time.split(":")[1][:2]) - st_time[1] 
                    if difference_time>20:
                        score -= 4
                    if difference_time>30:
                        score -= 4
            except:
                print(user,"time error")

            # Append the test file to the submission file and run the code
            try:
                with open(file_path, "a+") as task_file:
                        task_file.write(test_file)
            except:
                score = "no answer"
            cmd = f'python "{file_path}"'
            output = os.popen(cmd).read().replace("\n","")

            # Add the user's score to their task_data dictionary
            score += int(output.split("user-score-is:")[-1])

        except:
            print('error test')

        # Add the user's score and time difference to the task_data dictionary
        task_data['score']  += [score]
        task_data['time'] += [difference_time]
        task_data['user'] += [user]

        # Create a dataframe for the user's score and time difference and add it to the data dictionary
        df = pd.DataFrame(data={'score':[score],"time":[difference_time]})
        data[task] += [tabulate(df, headers = 'keys', tablefmt = 'psql' ,showindex = False)]
        data['user'] += [user]

    # Return the data and task_data dictionaries
    return data, task_data
