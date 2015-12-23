#!/usr/bin/python
#Answer 
#twitter
#Part 1: 
#Part 2:
#Github
#Part 1: 377891
#Part 2: 

#twitter input:
#s = ""
#github input: iwrupvqb
#Test
import re 
import string
import collections

alphabet = string.ascii_lowercase

def check_password(password):
    s = check_straight(password)
    i = check_iol(password)
    d = check_double(password)
    return s and i and d

def check_straight(password):
    for x in range(len(password[:-2])):
        index = alphabet.index(password[x])
        if index < 24 and password[x+1] == alphabet[(index+1)] and password[x+2] == alphabet[(index+2)]:
            return True
    return False

def check_iol(password):
    if password.find('i') != -1 or password.find('o') != -1 or password.find('l') != -1:
        return False
    return True

def check_double(password):
    double =[]
    for x in range(len(password[:-1])):
        if x not in double and password[x] == password[x+1]:
            double.append(x+1)

    return len(double) > 1

def find_next(password):
    p= 0
    for x,y  in zip(password,reversed(range(len(password)))):
        p+= alphabet.find(x)*26**y
    x = 1
    while(True):
        n = ''.join((alphabet[(p+x)//26**7%26],
                alphabet[((p+x)//26**6)%26],
                alphabet[((p+x)//26**5)%26],
                alphabet[((p+x)//26**4)%26],
                alphabet[((p+x)//26**3)%26],
                alphabet[((p+x)//26**2)%26],
                alphabet[((p+x)//26**1)%26],
                alphabet[((p+x)//26**0)%26]))
        if check_password(n):
            return n
        x +=1

def part1():
    check_password('hijklmmn')
    check_password('abbceffg')
    check_password('abbcegjk')
    check_password('abcdffaa')
    check_password('ghjaabcc')
    print(find_next('abcdefgh'))
    print(find_next('ghijklmn'))
    s = find_next('cqjxjnds')
    print('Part 1:',s)

def part2():
    s = find_next('cqjxxyzz')
    print('Part 2:',s)


part1()
part2()
