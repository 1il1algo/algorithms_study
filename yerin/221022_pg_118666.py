def solution(survey, choices):

    result ={'A' : 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'N' :0, 'R': 0, 'T': 0}
    for i in range(len(survey)):
        q = survey[i]
        a = choices[i]
        if 5 <= a <= 7 : result[q[1]] += a-4
        elif 1 <= a <= 3 : result[q[0]] += 4-a
    
    res_list = []
    if result['R'] >= result['T'] : res_list.append('R')
    else : res_list.append('T')
    
    if result['C'] >= result['F'] : res_list.append('C')
    else : res_list.append('F')
    
    if result['J'] >= result['M'] : res_list.append('J')
    else : res_list.append('M')
    
    if result['A'] >= result['N'] : res_list.append('A')
    else : res_list.append('N')
    
    answer = ''.join(res_list)
    return answer
