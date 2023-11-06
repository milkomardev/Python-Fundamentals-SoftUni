# def repeating_string(word, n):
#     result = word * n
#     return result


word = input()
count = int(input())

repeating_string = lambda word, count: word*count

print(repeating_string(word, count))
