#open the input file called data.txt
with open("data.txt","r+") as file:
#while loop iterates through the file
    while True:
        line = file.readline().strip()
        if line == '':
            break #break when EOF os reached
        colIndex=line.index(":")
        #error checking 
        if(len(line)>5):
            line=line[0:colIndex+3]
        #error checking for non digits or wrong position of : 
        if (colIndex > 2 or colIndex == -1 or not(line[0:colIndex].isdigit()) or not(line[colIndex+1:].isdigit())):
            print ("ERROR!")
            continue
        #storing hours and mins values in integer variables
        hours=int(line[0:colIndex])
        mins=int(line[colIndex+1:])
        #error checking for invalid time
        if (hours > 23 or mins > 59):
            print ("ERROR!")
            continue
        #converting military format to civilian
        if hours > 12:
            hours-=12
        #calculating degrees for  
        degree_hours = hours * 30
        degree_mins = mins * 6
        degree_hours += (mins*0.5)
        angle=abs(degree_hours-degree_mins)
#check if it is the smallest angle
        if((360-angle)<angle):
            angle=360-angle
        print (angle)

    file.close()    
    
