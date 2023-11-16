people_in_queue = int(input())
wagon_seats = [int(x) for x in input().split()]

# seats per wagon = 4

while people_in_queue >= 0:
    for wagon in range(len(wagon_seats)):
        diff = 4 - wagon_seats[wagon]
        if wagon_seats[wagon] < 4:
            wagon_seats[wagon] += min(diff, people_in_queue)
            people_in_queue -= min(diff, people_in_queue)

        elif wagon_seats[wagon] == 4:
            continue

    if sum(wagon_seats) == len(wagon_seats) * 4:
        if people_in_queue == 0:
            print(*wagon_seats, sep=' ')
            break
        else:
            print(f"There isn't enough space! {people_in_queue} people in a queue!")
            print(*wagon_seats, sep=' ')
            break
    else:
        print('The lift has empty spots!')
        print(*wagon_seats, sep=' ')
        break

