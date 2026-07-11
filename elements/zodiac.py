def define (Day, Month):
    zodiac = Month
    if Month < 13 and Month > 0 and Day < 32 and Day > 0: 
        if Day >= 22:
            zodiac += 1
        if zodiac > 12:
            zodiac = 1
        return zodiac
   
   
    else:
        return 0
print(define(11, 6))