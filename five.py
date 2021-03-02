import random
import math

dimensionX=0
dimensionY=0
print('Please give the width and height.The value of them must be equal or greater than 4')
while dimensionX<4: 
    userInputX=input("Give height")
    dimensionX=int(userInputX)
while dimensionY<4:
    userInputY=input("Give width")
    dimensionY=int(userInputY)



sum=0
for w in range(100):
    arr = [ ['O']*dimensionY for i in range(dimensionX)]

    numberOfCells=dimensionX*dimensionY

    halfNumberOfCells=math.ceil(numberOfCells/2)

    counter1=0
    filled=False
    while(counter1<halfNumberOfCells):
    
        for x in range(dimensionX):
            if filled==True:
                break
            for y in range(dimensionY):
                if  arr[x][y]!='S':
                    if random.randint(0,1)==1:
                        arr[x][y]='S'
                        counter1+= 1
                        if counter1==halfNumberOfCells:
                            filled=True
                            break
            
    print(arr)

    #horizontal
    counter=0
    for x in range(dimensionY):
        for y in range(1,(dimensionX-1)):
            if arr[y][x]=='O' and arr[y+1][x]=='S' and arr[y-1][x]=='S':
                counter=counter+1
                #print(x,y)



    #vertical

    for x in range(1,(dimensionY-1)):
        for y in range(dimensionX):
            if arr[y][x]=='O' and arr[y][x+1]=='S' and arr[y][x-1]=='S':
                counter=counter+1
                #print(x,y)


    #diagonical

    for x in range(1,(dimensionY-1)):
        for y in range(1,(dimensionX-1)):
            if arr[y][x]=='O':
                if arr[y-1][x-1]=='S' and arr[y+1][x+1]=='S':
                    counter=counter+1
                elif arr[y-1][x+1]=='S' and arr[y+1][x-1]=='S':
                    counter=counter+1
    
    print('SOS counter=')
    print(counter)
    sum+=counter
print('Average=')
print(sum/100)