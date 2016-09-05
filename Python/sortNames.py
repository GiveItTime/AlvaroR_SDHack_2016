
if __name__ == '__main__':
#	Author: Alvaro Rivas
#	Date: 4/29/16
#	Version: PyCharm Community Edition 4.0.5
#	Description:
#			Input: File contains a variable number of names, 1 name per line.
#			Output: Sorted file of names in the following format: 
#					last name first, followed by a comma and a space, followed by first name, followed by a space, then middle name or initial (if available). 
#					The names printed must be sorted in ascending A-Z order by last name.
#
#			Each name in input file starts with a first name, an optional middle name or middle initial, and a last name. 
#	===========================================================================================================================================================
    fileName = raw_input("Enter File Name: ")
#	Opens specified file by the user for reading
    try:
        inFile = open(fileName, 'r')
    except IOError:# Failure to open file
        print('An error occurred trying to read the file ', fileName)
        exit()
    tempFile = open('tempSortedNames.txt', 'w') #opens a file for writing; new file will store newly rearranged names
#	Splits up incoming string while looping through file
    for line in inFile:
        mylist = line.split()
        size = len(mylist)# stores size of newly split up string
#	Indexes into string if it's split into 3 parts and writes out rearranged string to file for safe storage
        if(size == 3):
            first = line.split()[0]
            middle = line.split()[1]
            last = line.split()[2]
            tempFile.write(last + ', ' + first + ', '  + middle + '\n')
#	Indexes into string if it's split into 2 parts and writes out rearranged string to file for safe storage
        if(size == 2):
            first = line.split()[0]
            last = line.split()[1]
            tempFile.write(last + ', ' + first + '\n')

    tempFile.close()# closes tempFile
    sortFile = open('tempSortedNames.txt','r')# reopens tempFile for reading
    tempL = [] # temporary array
    count = 0
#	Loops through file and stores file lines in temporary array
    for sline in sortFile:
        tempL.append(sline)
        count += 1
    tempL.sort() # sorts temporary array
#	Opens file for writing to store rearranged, newly sorted names
    outFile = open('sortedNames.txt', 'w')
#	Loops through an array, while writing out newly sorted temporary array to output file sortedNames.txt 
    for index in range(0,count):
        outFile.write(tempL[index])
    inFile.close() # closes user file
    outFile.close()# closes sortedNames.txt file