def solution(survey, choices):
    res = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    result = ""
    for idx, choice in enumerate(choices):
        if choice > 4:
            grade = choice - 4
            res[survey[idx][1]] += grade
        elif choice < 4:
            grade = 4 - choice
            res[survey[idx][0]] += grade
    
    print(res)
    
    if res["R"] >= res["T"]:    result += "R"
    else:   result += "T"
    
    if res["C"] >= res["F"]:    result += "C"
    else:   result += "F"
    
    if res["J"] >= res["M"]:    result += "J"
    else:   result += "M"
    
    if res["A"] >= res["N"]:    result += "A"
    else:   result += "N"
    
    return result