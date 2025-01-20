#!/usr/bin/python3

# Objectives:
#   1. Take filename path from user input
#   2. Use python standard dictionary as main data structure
#   3. Read the log file data from /var/log/auth.log
#   4. Save data into the dictionary data structure
#   5. Output analysis results to std output, notably:
#   
#   Overall Statistics
#       - # of total Login attempts by Unique IP's
#       - # of total Unique IPs Attempted to Login
#       - # of total Unique IPs with successful logins
#       - # of total Unique IPs with failed logins
#
#   Indepth Data
#       - List each Unique IP
#           - List all usernames it attempted to login to
#           - List # of successful logins
#           - List # of failed logins
#
#   6. Use PEP8 STYLING GUIDE

def analyse_auth_log(filepath):

# 1. Open handle to the file

    auth_log_file = open(filepath, "r")
    print(auth_log_file.read())

# 2. Start from beginning, iterate through whole file line by line
# 3. Read data into dictionary

def main():
    auth_log_file_path = input("Enter the auth log file path: ")
    analyse_auth_log(auth_log_file_path)

if __name__ == "__main__":
    main()

