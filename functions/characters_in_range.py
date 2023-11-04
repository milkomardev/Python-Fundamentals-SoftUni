def get_char_in_range(a, b):
    result = []
    for n in range(ord(a) + 1, ord(b)):
        result.append(chr(n))

    return result


start = input()
end = input()

result_chars = get_char_in_range(start, end)

print(' '.join(result_chars))
