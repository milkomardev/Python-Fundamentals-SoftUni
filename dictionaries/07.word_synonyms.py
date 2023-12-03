count_of_words = int(input())
synonyms = {}

for n in range(count_of_words):
    word = input()
    syn = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(syn)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
