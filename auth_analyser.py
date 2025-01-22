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
#       - # of total SSHD sessions
#
#   Indepth Data
#       - List each Unique IP
#           - List all usernames it attempted to login to
#           - List # of successful logins
#           - List # of failed logins
#
#   6. Use PEP8 STYLING GUIDE

authlog_summary = {}

def log_message_extracter(log_msg):
    """
    
    
    """
    print(f"{log_msg.strip()}")

    # First interpret what the log message is

    if "Failed password for invalid user" in log_msg:
        print("-- 1st String Found\n")
    elif "Failed password for" in log_msg:
        print("-- 2nd String Found\n")
    elif "Invalid user" in log_msg:
        print("-- 3rd String Found\n")
    elif "Accepted publickey for" in log_msg:
        print("-- 4th String Found")
    elif "Unable to negotiate with" in log_msg:
        print("-- 5th String Found")
    elif "fatal: userauth_pubkey: parse publickey packet: incomplete message" in log_msg:
        print("-- 6th String Found")
    elif "error: kex_protocol_error" in log_msg:
        print("-- 7th String Found")
    elif "Connection reset by invalid user" in log_msg:
        print("-- 8th String Found")
    elif "Connection reset by" in log_msg:
        print("-- 9th String Found")
    else:
        print("\n")

    # Second extract the relevant data from the log message (if applicable)
    # Third enter into the dictionary

def analyse_auth_log(filepath):
    """ Iterates over each line in the auth log
    
    Args:
        filepath: path to the auth.log file

    Returns:
        <Nothing yet>

    """
    with open(filepath, "r") as auth_log_file:
        for line_num, line in enumerate(auth_log_file, start=1):
            if "sshd[" in line:
                # Get the log message seperately
                log_message_extracter(line[59:])

            else: 
                # Later revision?
                print(f"Omitting Line #{line_num}, not an sshd log message\n")
def main():
    auth_log_file_path = input("Enter the auth log file path: ")
    analyse_auth_log(auth_log_file_path)

if __name__ == "__main__":
    main()

