"""

Written By: Gil Rael

The following program prompts the user for the protocol either http or https,
user_name and password and then exports that protocol for proxy authentication


"""


import os



def obtain_user_information():
    user_name = raw_input("Enter your username.")
    print(user_name)
    pw = raw_input("Enter your password.")
    print(pw)
    protocol = raw_input("Enter protocol either http or https.")
    print(protocol)
    command = "export " + '"' + (protocol) + "_proxy=" + (protocol) + "://" + (user_name) + ":" + (pw) + "@proxyout.lanl.gov:8080" + '"'
    print(command)
    os.popen(command, 'w')
obtain_user_information()
