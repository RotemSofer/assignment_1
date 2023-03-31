#################################### Q1 ###########################################
def my_func(x1,x2,x3):
    if type(x1) != float or type(x2) != float or type(x3) != float:
        if x1 == 0 and x2 == 0 and x3 == 0:
            return "Not a number - denominator equals zero"
        if type(x1) != int and type(x1) != float or type(x2) != int and type(x2) != float or type(x3) != int and type(x3) != float:
            return None
        else:
            return "Error: parameters should be float"
    else:
        numerator = ((x1+x2+x3)*(x2+x3)*x3)
        denominator = (x1+x2+x3)
        if denominator == 0:
            result = "Not a number - denominator equals zero"
        else:
            result = float(numerator/denominator)
        return result
print(my_func())

#################################### Q2 ###########################################
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








