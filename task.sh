#!/bin/bash

#Write BASH script which takes one arg as input. In script, check the type of the arg and perform an action:
#1) if it is ELF executable, print ".rodata" section of the file (hint: use 'readelf') 
#2) if arg name ends with ".txt", append the current time to the end of this file 
#3) if arg is a number (integer number) and it is a PID of running process, print the 'cmdline' used to run this process (hint: use /proc/ subsystem), 
#    if not a PID - add '1000' and print this sum to console

# Check if the argument is an ELF executable
if file "$1" | grep -q "ELF"; then
    # Print the .rodata section of the file
    readelf -S "$1" | grep '.rodata'

# Check if the argument is a .txt file
elif [[ "$1" == *.txt ]]; then
    # Append the current time to the end of the file
    echo $(date) >> "$1"

# Check if the argument is a number
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    # Check if the argument is a PID of a running process
    if [[ -d /proc/$1 ]]; then
        # Print the cmdline used to run the process
        cat /proc/$1/cmdline
    else
        # Add 1000 to the argument and print the sum
        echo $(( $1 + 1000 ))
    fi
else
    echo "Invalid argument"
fi