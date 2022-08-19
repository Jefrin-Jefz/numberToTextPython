def start_conversion(x):
    num = x    
    digits=list(str(num))
    function_list[-len(digits)] (digits)
    return answer                   
ones_number=["zero","one","two","three","four",'five',"six","seven","eight","nine"]
tens_number=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
elevens_number=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seveteen","eighteen","nineteen"]

answer=[]

def mil_word (digits):             
    answer.append(str(ones_number[int(digits[-7])]+"_million "))   #for 1234567

    htou_word (digits)

def htou_word (digits):
    if int(digits[-6]) == 0 and int(digits[-5]) == 0 :          #for 001,000
        tou_word (digits)
    elif int(digits[-6]) == 0 and int(digits[-5]) != 0 :        #for 010,000
        ttou_word (digits)

    elif int(digits[-6]) != 0 and (int(digits[-5]) == 0 and int(digits[-4]) == 0):        #100,000 , 200,000
        answer.append(str(ones_number[int(digits[-6])]+"_hundred thousand"))                       #prints - one +hundered thousand
        hun_word (digits)

    elif int(digits[-6]) != 0 :            #110,000 , 102,000
        answer.append(str(ones_number[int(digits[-6])]+"_hundred and "))         #prints - one + hundred and
        ttou_word (digits)
  
def ttou_word (digits):
    if int(digits[-5]) == 0 and int(digits[-4]) == 0 :          #for 00,100
        hun_word (digits)

    elif int(digits[-5]) == 0 and int(digits[-4]) != 0 :        #for 01,000
        tou_word (digits)
    
    elif int(digits[-5]) != 0 and int(digits[-4]) == 0:                   #10,000 , 20,000
        answer.append(str(tens_number[int(digits[-5])-1] + "_thousand"))              #prints - one + thousand
    
    elif int(digits[-5]) == 1 and int(digits[-4]) != 0:                 #11,000 , 12,000
        answer.append(str(elevens_number[int(digits[-4])-1] + "_thousand"))           #prints - eleven + thousand

    elif int(digits[-5]) > 1 and int(digits[-4]) != 0:        #21,000 , 31,000
        answer.append(str(tens_number[int(digits[-5])-1])+" ")                #prints - twenty ,thirty
        tou_word (digits)

def tou_word (digits):
    if int(digits[-4]) != 0 :                                             #1,000 , 2,000
        answer.append(str(ones_number[int(digits[-4])]+"_thousand and "))         #prints - one + thousand, two + thousand
    hun_word (digits)

def hun_word (digits):
    if int(digits[-3]) == 0 and (int(digits[-2]) == 0 and int(digits[-1]) == 0):         #for 000
        pass

    elif int(digits[-3]) == 0 and (int(digits[-2]) == 0 and int(digits[-1]) != 0):         #for 001
        one_word (digits)
    
    elif int(digits[-3]) == 0 and int(digits[-2]) != 0 :        #for 010
        ten_word (digits)

    elif int(digits[-3] != 0) and (int(digits[-2]) == 0 and int(digits[-1]) == 0) :            #for 100,200
        answer.append(str("and " + ones_number[int(digits[-3])]+"_hundred" ))                                          #prints - one + hundred

    elif int(digits[-3] != 0) :                                                         #for 123,110,101
        answer.append(str(ones_number[int(digits[-3])]+"_hundred and " ))                               #prints - one + hundred and
        ten_word (digits)   

def ten_word (digits):
    if int(digits[-2]) == 0 and int(digits[-1] == 0):              #for 01
        pass

    elif int(digits[-1]) == 0:
        answer.append(str(tens_number[int(digits[-2])-1])+" ")           #for 20    prints twenty

    elif int(digits[-2]) == 1 :
        answer.append(str(elevens_number[int(digits[-1])-1], ))       #for 11

    elif int(digits[-1]) != 0:                         #for 21
        answer.append(str(tens_number[int(digits[-2])-1])+" ") 
        one_word (digits)

def one_word (digits):
        answer.append(str(ones_number[int(digits[-1])])) 

function_list = [mil_word,htou_word,ttou_word,tou_word,hun_word,ten_word,one_word]