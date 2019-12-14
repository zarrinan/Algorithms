#!/usr/bin/python

import sys


def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
  

def strev(str): 
    len = len(str); 
    for i in range(int(len / 2)): 
        temp = str[i]; 
        str[i] = str[len - i - 1]; 
        str[len - i - 1] = temp; 


def fromDeci(base, inputNum): 
    res = ""
    index = 0; # Initialize index of result 
  
    # Convert input number is given base  
    # by repeatedly dividing it by base  
    # and taking remainder 
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base); 
  
    # Reverse the result 
    res = res[::-1]; 
  
    return res


def rock_paper_scissors(n):
    r = []
    ro = [('rock', 0), ('paper', 1), ('scissors', 2)]
    l3n = len(str(fromDeci(3,3**n - 1))) 
    for i in range(3 ** n):
        b3 = str(fromDeci(3, i)).zfill(l3n)
        lr = []
        for j in range(n):
            lr.append(ro[int(b3[j])][0])
        r.append(lr)
    return r



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')