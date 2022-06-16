"""
Created on Thu Jan 20 10:34:27 2022

@author: hbrazal

"""


from nltk.corpus import words
import pandas as pd
from collections import Counter
import os

os.getcwd()

 

   

def split(word):
    return [char for char in word]

 

 

dictionary= pd.DataFrame(words.words())
dictionary= dictionary.rename(columns={0: "word"})
dictionary['count']=dictionary.iloc[:,0].str.len()
word5= dictionary[dictionary['count']==5]
word5=word5.reset_index(drop=True)
word5['word']= word5['word'].astype(str)
 

morewds= pd.read_excel(r'C:/Users/28mac/Documents/Python Code/5worddict.xlsx')
morewds= morewds.rename(columns={'aback':'word'})
word5= word5.append(morewds)

 

word5=word5.drop_duplicates(subset=['word'])
word5=word5.drop(columns=['count'])
word5=word5.sort_values(by=['word'])
word5=word5.reset_index(drop=True)
#drop the proper names
word5=word5.iloc[1734:,:].reset_index(drop=True)

 
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_points = {letter:point for letter, point in zip(letters,points)}

 #Establish the score of a given word, need the upper since the dictionary is all upper, if any double letter then add a point

def score(word):
   totpoints = 0
   for x in word:
        totpoints = totpoints + letter_points[x.upper()]
    
   if len(set(split(word))) == 5:
    return totpoints
   else:
    return (totpoints+1)

 
word5["score"]= ""
for i in range(len(word5)):
    word5.iloc[i,1]=score(word5.iloc[i,0])

 

 



############# MANUAL CODE-----------

 

# raise, crane, later, arose, soare, share, sauce, tears, stare    


if 'w1' in globals():
    del w1

if 'w2' in globals():
    del w2
if 'w3' in globals():
    del w3
if 'w4' in globals():
    del w4
if 'w5' in globals():
    del w5
if 'y1' in globals():
    del y1
if 'y2' in globals():
    del y2
if 'y3' in globals():
    del y3
if 'y4' in globals():
    del y4
if 'y5' in globals():
    del y5   
    
w1=""
w2=""
w3=""
w4=""
w5=""   
 
y1lts=[]
y2lts=[]
y3lts=[]
y4lts=[]
y5lts=[]

blets=[]   
nolet= input("Gray letters? :")
blets.extend(list(nolet))


ulets=[]  
ulet= input("Letters in the word? :")
ulets.extend(list(ulet))

blets=list((Counter(blets)-Counter(ulets)).elements())
#run with nothing else

ngs=[i for i in word5['word'] if all(j not in i for j in blets)] 

#with yellows

ngs1=sorted([i for i in ngs if all(j in i for j in ulets)])

# print(ngs1)

#most used letters in order- e,t,a,i,n,o,s,h,r,d,l,u,c,n,f,w,y,g,p,b.v.k.q,j,x,z

#non crane vowels- would want something with t and i maybe n and o

'''
toplets=[]
toplet= input("Which letters do you want to have? ")
toplets.extend(list(toplet))
print(sorted([i for i in ngs1 if all(j in i for j in toplet)]))
'''

try:
    a1=input("Letter in space 1? ")
    if a1=="y":
        a1a= input("Green or Yellow (g/y)? ")
        if a1a=="g":
            w1=input("what's the letter? ")
        if a1a=="y":
            y1=input("what's the letter? ")
    y1lts.extend(list(y1))
except NameError:
    pass
try:
    a2=input("Letter in space 2? ")
    if a2=="y":
        a2a= input("Green or Yellow (g/y)? ")
        if a2a=="g":
            w2=input("what's the letter? ")
        if a2a=="y":
            y2=input("what's the letter? ")
    y2lts.extend(list(y2))
except NameError:
    pass   
try:
    a3=input("Letter in space 3? ")
    if a3=="y":
        a3a= input("Green or Yellow (g/y)? ")
        if a3a=="g":
            w3=input("what's the letter? ")
        if a3a=="y":
            y3=input("what's the letter? ")
    y3lts.extend(list(y3))
except NameError:
    pass
try:
    a4=input("Letter in space 4? ")
    if a4=="y":
        a4a= input("Green or Yellow (g/y)? ")
        if a4a=="g":
            w4=input("what's the letter? ")
        if a4a=="y":
            y4=input("what's the letter? ")
    y4lts.extend(list(y4))
except NameError:
    pass
try:
    a5=input("Letter in space 5? ")
    if a5=="y":
        a5a= input("Green or Yellow (g/y)? ")
        if a5a=="g":
            w5=input("what's the letter? ")
        if a5a=="y":
            y5=input("what's the letter? ")
    y5lts.extend(list(y5))
except NameError:
    pass


#green letters
wordfilt=[]
for i in range(len(ngs1)):
    if (ngs1[i].find(w1,0)==0 and
            ngs1[i].find(w2,1)==1 and
            ngs1[i].find(w3,2)==2   and
            ngs1[i].find(w4,3)==3    and
            ngs1[i].find(w5,4)==4 ):   
            
            wordfilt.append(ngs1[i])
 
# print(sorted(set(wordfilt)))

wordfilty=[]
try:
    [[wordfilty.append(ngs1[i]) for k in range(len(y1lts)) if ngs1[i].find(y1lts[k],0)==0] for i in range(len(ngs1))]
except NameError:
    pass
try:
    [[wordfilty.append(ngs1[i]) for k in range(len(y2lts)) if ngs1[i].find(y2lts[k],1)==1] for i in range(len(ngs1))]
except NameError:
    pass
try:
    [[wordfilty.append(ngs1[i]) for k in range(len(y3lts)) if ngs1[i].find(y3lts[k],2)==2] for i in range(len(ngs1))]
except NameError:
    pass
try:
    [[wordfilty.append(ngs1[i]) for k in range(len(y4lts)) if ngs1[i].find(y4lts[k],3)==3] for i in range(len(ngs1))]
except NameError:
    pass
try:
    [[wordfilty.append(ngs1[i]) for k in range(len(y5lts)) if ngs1[i].find(y5lts[k],4)==4] for i in range(len(ngs1))]
except NameError:
    pass
 

filtyout=list((Counter(ngs1)-Counter(wordfilty)).elements())

# print(filtyout)

 
if len(wordfilt)!=0 and len(filtyout)!=0:
    filtset = set(wordfilt)
    intersection = filtset.intersection(filtyout)
    intersectionl= list(intersection)
    wscor=pd.DataFrame(intersectionl, columns=['word'])
    wscor=pd.merge(wscor, word5)
    print(wscor.sort_values(by=['score']))
elif len(filtyout)==0:
     wscor=pd.DataFrame(wordfilt, columns=['word'])
     wscor=pd.merge(wscor, word5)
     print(wscor.sort_values(by=['score']))
else:
    wscor=pd.DataFrame(filtyout, columns=['word'])
    wscor=pd.merge(wscor, word5)
    print(wscor.sort_values(by=['score']))


#use space then join whatever
letuse= "".join([i for i in wscor["word"]])

print(Counter(letuse).most_common())

common1st= "".join([i for i in wscor["word"]])
#since all words are 5 letters
common1st=common1st[0::5]
print(Counter(common1st).most_common())






#word5[word5["word"]=="fjord"]

