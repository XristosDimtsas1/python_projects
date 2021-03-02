import random
import math

print("Please give the square's dimension,which must be equal or greater than 4")
squareDimension=0
while squareDimension<4:
    userInput=input("Give the square's dimension")
    squareDimension=int(userInput)


sum=0
for w in range(100):
    arr = [ [None]*squareDimension for i in range(squareDimension)]



    numberOfCells=squareDimension*squareDimension

    halfNumberOfCells=math.ceil(numberOfCells/2)

    counter1=0
    filled=False
    while(counter1<halfNumberOfCells):
        for x in range(squareDimension):
            if filled==True:
                break
            for y in range(squareDimension):
                if  arr[x][y]!=1:
                    if random.randint(0,1)==1:
                        arr[x][y]=1
                        counter1+= 1
                        if counter1==halfNumberOfCells:
                            filled=True
                            break
            
    print(arr)

    counter=0
    #vertical
    for x in range(squareDimension):
        for y in range((squareDimension-3)):
            if arr[y][x]==1 and arr[y+1][x]==1 and arr[y+2][x]==1 and arr[y+3][x]==1:
                counter=counter+1
            

    #horizontal
    for x in range(squareDimension-3):
        for y in range((squareDimension)):
            if arr[y][x]==1 and arr[y][x+1]==1 and arr[y][x+2]==1 and arr[y][x+3]==1:
                counter=counter+1


    #diagonical

    for x in range(squareDimension):
        for y in range(squareDimension-3):
            if arr[x][y]==1 and x+3<squareDimension and y+3<squareDimension:
                if arr[x+1][y+1]==1 and arr[x+2][y+2]==1 and arr[x+3][y+3]==1 :
                    counter=counter+1
                


    for x in range(squareDimension):
        for y in range(squareDimension-1,2,-1):
            if arr[x][y]==1 and x+3<squareDimension:
                if arr[x+1][y-1]==1 and arr[x+2][y-2]==1 and arr[x+3][y-3]==1:
                    counter=counter+1
                
    print('Four continuous 1 counter=')
    print(counter)
    sum+=counter
print('Average=')
print(sum/100)



















        






