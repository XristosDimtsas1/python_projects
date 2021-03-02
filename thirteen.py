import re
#read files and store lines into a list of strings
with open(r'C:\Users\xrist\OneDrive\Υπολογιστής\two_cities_ascii.txt')as f:
    lines=f.readlines()
    

romain_numbers_list=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX'
,'XX','XXI','XXII','XXIII','XXIV']
words=[]       
for line in lines:
    for word in line.split():
        if word not in romain_numbers_list:
            words.append(''.join(filter(str.isalpha,word)))


words_duplicated=words.copy()
for word1 in words:
    words_duplicated.remove(word1)
    for word2 in words_duplicated:
        if len(word2)+len(word1)==20:
            words.remove(word1)
            words.remove(word2)
            words_duplicated.remove(word2)
            print(word1+"-"+word2)
            break



    
        





            