def my_func(x1,x2,x3):
    if type(x1) != float or type(x2) != float or type(x3) != float:
        print("Error: paramaters should be float")
        return None
    else:
        numerator = ((x1+x2+x3)*(x2+x3)*x3)
        denominator = (x1+x2+x3)
        if denominator == 0:
            result = "Not a number - denominator equals zero"
        else:
            result = float(numerator/denominator)
        return result
#print(my_func(4,5,6))

#######################################
def revword(word:str):
    word = word.lower()[::-1]
    return word

def countword():
    count = 0
    text = open('text.txt','r')
    for line in text:
        line = line.split()
        if len(line) == 1:
            word = line[0]
            count += 1
        else:
            for words in line:
                rev_w = revword(words)
                if rev_w == word:
                    count += 1
    print(count)

countword()








