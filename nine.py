import math
#read files and store lines into a list of strings
with open(r'C:\Users\xrist\OneDrive\Υπολογιστής\two_cities_ascii.txt')as f:
    lines=f.readlines()
    

asciiNums=[]
#convert each character into ascii number and store the numbers into asciiNums
for line in lines:
    for c in line:
        
        asciinumber=ord(c)
        asciiNums.append(asciinumber)


#remove even numbers
asciiNums_without_evenNumbers=[]
for num in asciiNums:
    if num%2!=0:
        asciiNums_without_evenNumbers.append(num)



letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
appear_times=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
    for s in line:
        appear_times[0]=appear_times[0]+s.count('a')
        appear_times[0]=appear_times[0]+s.count('A')

        appear_times[1]=appear_times[1]+s.count('b')
        appear_times[1]=appear_times[1]+s.count('B')

        appear_times[2]=appear_times[2]+s.count('c')
        appear_times[2]=appear_times[2]+s.count('C')

        appear_times[3]=appear_times[3]+s.count('d')
        appear_times[3]=appear_times[3]+s.count('D')
        
        appear_times[4]=appear_times[4]+s.count('e')
        appear_times[4]=appear_times[4]+s.count('E')

        appear_times[5]=appear_times[5]+s.count('f')
        appear_times[5]=appear_times[5]+s.count('F')

        appear_times[6]=appear_times[6]+s.count('g')
        appear_times[6]=appear_times[6]+s.count('G')

        appear_times[7]=appear_times[7]+s.count('h')
        appear_times[7]=appear_times[7]+s.count('H')

        appear_times[8]=appear_times[8]+s.count('i')
        appear_times[8]=appear_times[8]+s.count('I')

        appear_times[9]=appear_times[9]+s.count('j')
        appear_times[9]=appear_times[9]+s.count('J')

        appear_times[10]=appear_times[10]+s.count('k')
        appear_times[10]=appear_times[10]+s.count('K')

        appear_times[11]=appear_times[11]+s.count('l')
        appear_times[11]=appear_times[11]+s.count('L')

        appear_times[12]=appear_times[12]+s.count('m')
        appear_times[12]=appear_times[12]+s.count('M')

        appear_times[13]=appear_times[13]+s.count('n')
        appear_times[13]=appear_times[13]+s.count('N')

        appear_times[14]=appear_times[14]+s.count('o')
        appear_times[14]=appear_times[14]+s.count('O')

        appear_times[15]=appear_times[15]+s.count('p')
        appear_times[15]=appear_times[15]+s.count('P')

        appear_times[16]=appear_times[16]+s.count('q')
        appear_times[16]=appear_times[16]+s.count('Q')

        appear_times[17]=appear_times[17]+s.count('r')
        appear_times[17]=appear_times[17]+s.count('R')

        appear_times[18]=appear_times[18]+s.count('s')
        appear_times[18]=appear_times[18]+s.count('S')

        appear_times[19]=appear_times[19]+s.count('t')
        appear_times[19]=appear_times[19]+s.count('T')

        appear_times[20]=appear_times[20]+s.count('u')
        appear_times[20]=appear_times[20]+s.count('U')

        appear_times[21]=appear_times[21]+s.count('v')
        appear_times[21]=appear_times[21]+s.count('V')

        appear_times[22]=appear_times[22]+s.count('w')
        appear_times[22]=appear_times[22]+s.count('W')

        appear_times[23]=appear_times[23]+s.count('x')
        appear_times[23]=appear_times[23]+s.count('X')

        appear_times[24]=appear_times[24]+s.count('y')
        appear_times[24]=appear_times[24]+s.count('Y')

        appear_times[25]=appear_times[25]+s.count('z')
        appear_times[25]=appear_times[25]+s.count('Z')

#sum letters appearances
letters_sum=0
for num in appear_times:
    letters_sum+=num

statistic_number=0
output=""
for i in range(26):
    statistic_number=math.ceil(appear_times[i]*100/letters_sum)
    
    output=letters[i]+": "
    
    for k in range(statistic_number):
        output+="* "
    print(output)
    output=""




        
