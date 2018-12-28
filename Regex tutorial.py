import re

def match():
    text="1 3eqwewem33224 3 435343 3fefe5eeed 3 5 6 4rtrtmlr44 5"
    inletters=['zero','one','two','three','four','five','six','seven','eight','nine']
    ptr=re.compile(r'\b\d\b')
    result=re.findall(ptr,text)
    for x in range(len(result)):
        ind=int(result[x])
        newpattern=r"\b"+result[x]+r"\b"
        text=re.sub(newpattern,inletters[ind],text)
    print (text)
match()
