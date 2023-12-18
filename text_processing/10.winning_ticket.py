def get_best_result(ticket, symbol):
    best_result = ''
    current_result = ''
    for ch in ticket:
        if ch == symbol:
            current_result += ch
            if len(current_result) > len(best_result):
                best_result = current_result
        else:
            current_result = ''
    return len(best_result)


tickets = [ticket.strip() for ticket in input().split(', ')]
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue

    first_half = ticket[:10]
    second_half = ticket[10:]
    best_result = 0
    best_symbol = ''


    for symbol in symbols:
        first_half_score = get_best_result(first_half, symbol)
        second_half_score = get_best_result(second_half, symbol)
        result = min(first_half_score,second_half_score)
        if result > best_result:
            best_result = result
            best_symbol = symbol

    is_winning = best_result >= 6

    if is_winning and best_result == 10:
        print(f'ticket "{ticket}" - {best_result}{best_symbol} Jackpot!')
    elif is_winning:
        print(f'ticket "{ticket}" - {best_result}{best_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')
