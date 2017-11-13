def is_isogram(string):
    string = list(string.lower())
    count = []
    for i in string:
        if i == '-' or i == ' ':
            continue
        count.append(string.count(i))
    return all(i == 1 for i in count)
        
    
    
print(is_isogram(input('Give me a string')))
