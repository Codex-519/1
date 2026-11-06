#2. Student Performance Analyzer
fcount=pcount=gcount=ecount=0
for i in range(10):
    marks=int(input("Enter marks:"))
    if 100>=marks>=75:
        ecount+=1
        print("Excellent")
    elif 74>=marks>=50:
        gcount+=1
        print("Good")    
    elif 49>=marks>=35:
        pcount+=1
        print("Pass")
    elif 0<=marks<35:
        fcount+=1
        print("Fail")        
    else:
        print("please enter marks in range 0 to 100")
print("In Excellent category number of students is:",ecount)
print("In Good category number of students is:",gcount)
print("In Pass category number of students is:",pcount)
print("In Fail category number of students is:",fcount)



#3. Word Score Calculator
string=input("Enter paragraph:")
letters=string.split()
highest_score=0
highest_score_word=""
for letter in letters:
    score=0
    for i in letter:
        if i in "AEIOUaeiou":
            score+=2
        elif i not in "AEIOUaeiou":
            score+=1    
        elif chr(48)<=i<=chr(57):
            scoret+=3  
        else:
            score+=4
    if highest_score<score:
        highest_score=score
        highest_score_word=letter
print("Highest scoring word is:",highest_score_word)          
print("Score:", highest_score)



#4. Password Batch Validator
for i in range(5):
    ucount=lcount=dcount=sccount=islen=False
    passwords=input("Enter password:")
    for char in passwords:
        if len(passwords)>=8:
            islen=True
        if chr(65)<=char<=chr(90):
            ucount=True
        elif chr(97)<=char<=chr(122):
            lcount=True
        elif chr(48)<=char<=chr(57):
            dcount=True
        else:
            sccount=True  
    score=int(islen)+int(ucount)+int(lcount)+int(dcount)+int(sccount)      
    if score>=5:
        print("Password is Strong") 
    elif score>=3:
        print("Password is Medium")    
    else:
        print("Password is Weak")      



#5. Sentence Word Analyzer
Sentence=input("Enter Sentence:")
words=Sentence.split()
short_count=medium_count=long_count=0
for word in words:
    word_char_count=0
    print("The length of",word,"is",len(word))
    for i in word:
        word_char_count+=1
    if word_char_count<=3:
        short_count+=1
        print("word is short")
    elif word_char_count<6:
        medium_count+=1
        print("medium")    
    else:
        long_count+=1
        print("long")    
print("The short word in sentance is:",short_count)        
print("The medium word in sentance is:",medium_count)        
print("The long word in sentance is:",long_count)  