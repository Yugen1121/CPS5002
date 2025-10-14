# very cold (-10, 0, 10)
# cold (0, 10, 20)
# warm (10, 20, 30)
# Very warm, 20, 30, 40
# hot 30, 40 , 50

def FuzzyTemp(temp):
    dic = {
        "Very cold": (-10, 0, 10),
        "cold": (0, 10, 20),
        "Warm": (10, 20, 30),
        "Very warm": (20, 30, 40),
        "Hot": (30, 40, 50),
    }
    answer = ()
    for i, (low, middle, high) in dic.items():
        likely = 0
        if temp < low:
            likely = 0
        elif low <= temp <= middle:
            try:
                likely = (temp-low)/(middle-temp)
            except ZeroDivisionError:
                likely = 1
        elif middle <= temp <= high:
            likeyly = (high-temp)/(high-middle)
        else:
            likely = 0
        if not answer:
            answer = (i, likely) 
        elif answer[1]<likely:
            answer = (i, likely)
    
    return answer
    
print(FuzzyTemp(20))