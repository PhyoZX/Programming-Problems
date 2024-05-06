def string_match(a, b) :
    if len(a) < 2 or len(b) < 2 :
        return 0
    count = 0
    for i in range(min(len(a),len(b))-1) :
        if a[i] == b[i] and a[i + 1] == b[i + 1] :
            count += 1
    return count            

print(string_match('abcd','abc'))