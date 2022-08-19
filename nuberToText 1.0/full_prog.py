while True:
    num=int(input("enter the number"))
    if num > 9999999:
        print("enter a number in million range")
        continue
    break       
str(num)
digits=list(str(num))
n=len(digits)

ones_number=["zero","one","two","three","four",'five',"six","seven","eight","nine"]
tens_number=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
elevens_number=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seveteen","eighteen","nineteen"]


def mil_word():             
    print(ones_number[int(digits[-7])]+"_million",end=" ")      #for 1234567

    htou_word()

def htou_word():

    if int(digits[-6]) == 0 and int(digits[-5]) == 0 :          #for 001,000
        tou_word()
    elif int(digits[-6]) == 0 and int(digits[-5]) != 0 :        #for 010,000
        ttou_word()

    elif int(digits[-6]) != 0 and (int(digits[-5]) == 0 and int(digits[-4]) == 0):        #100,000 , 200,000
        print(ones_number[int(digits[-6])]+"_hundred thousand",end=" ")                       #prints - one +hundered thousand
        hun_word()

    elif int(digits[-6]) != 0 :            #110,000 , 102,000
        print(ones_number[int(digits[-6])]+"_hundred and",end=" ")         #prints - one + hundred and
        ttou_word()

    else:
        pass
    
  
def ttou_word():
    
    if int(digits[-5]) == 0 and int(digits[-4]) == 0 :          #for 00,100
        hun_word()

    elif int(digits[-5]) == 0 and int(digits[-4]) != 0 :        #for 01,000
        tou_word()
    
    elif int(digits[-5]) != 0 and int(digits[-4]) == 0:                   #10,000 , 20,000
        print(tens_number[int(digits[-5])-1] + "_thousand",end=" ")              #prints - one + thousand
    
    elif int(digits[-5]) == 1 and int(digits[-4]) != 0:                 #11,000 , 12,000
        print(elevens_number[int(digits[-4])-1] + "_thousand",end=" ")           #prints - eleven + thousand

    elif int(digits[-5]) > 1 and int(digits[-4]) != 0:        #21,000 , 31,000
        print(tens_number[int(digits[-5])-1],end="_")                #prints - twenty ,thirty
        tou_word()

    else:
        pass
    
def tou_word():                                             #1,000 , 2,000
    print(ones_number[int(digits[-4])]+"_thousand",end=" ")         #prints - one + thousand, two + thousand
    hun_word()

def hun_word():

    if int(digits[-3]) == 0 and int(digits[-2]) == 0 :         #for 001
        one_word()
    
    elif int(digits[-3]) == 0 and int(digits[-2]) != 0 :        #for 010
        ten_word()

    elif int(digits[-3] != 0) and (int(digits[-2]) == 0 and int(digits[-1]) == 0) :            #for 100,200
        print("and " + ones_number[int(digits[-3])]+"_hundred",end=" ")                                          #prints - one + hundred
        quit()

    elif int(digits[-3] != 0) :                                                         #for 123,110,101
        print(ones_number[int(digits[-3])]+"_hundred and",end=" ")                               #prints - one + hundred and
        ten_word()

    else:
        pass

def ten_word():

    if int(digits[-2]) == 0:              #for 01
        one_word()
    
    elif int(digits[-1]) == 0:
        print(tens_number[int(digits[-2])-1],end="")           #for 20    prints twenty
        quit()

    elif int(digits[-2]) == 1 :
        print(elevens_number[int(digits[-1])-1],end="")       #for 11
        quit()

    elif int(digits[-1]) != 0:                         #for 21
        print(tens_number[int(digits[-2])-1],end="_") 
        one_word()

def one_word():
    print(ones_number[int(digits[-1])])              

function_list = [mil_word,htou_word,ttou_word,tou_word,hun_word,ten_word,one_word]
function_list[-len(digits)]()
