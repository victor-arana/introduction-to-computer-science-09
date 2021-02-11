def count_bobs(string):
    count = 0
    i = 0
    while i < ( len(string) - 2):
        if string[i:i+3] == 'bob':
            count = count + 1
        i = i + 1
    return count

string = 'azcbobobegghakl'
print('Number of times bob occurs is', count_bobs(string))
