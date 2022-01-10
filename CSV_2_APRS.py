#Import needed library for CSV processing
import csv

#Open the date.csv file as read
with open('date.csv', 'r') as csvfile:
    #fetch the last line of the file, and then split it by the comma
    last_line = csvfile.readlines()[-1].split(',')
    
    #Create a string based on the different elements of last_line
    print(last_line[0], last_line[1], last_line[8], last_line[9], last_line[10], last_line[12])

    #shutdown the program safely
    exit()
