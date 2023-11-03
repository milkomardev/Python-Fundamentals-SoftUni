l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l3 = [int(x) for x in input().split()]

won_first = False
won_second = False
draw = False

if (l1[0] == 1 and l1[1] == 1 and l1[2] == 1) or \
    (l2[0] == 1 and l2[1] == 1 and l2[2] == 1) or \
    (l3[0] == 1 and l3[1] == 1 and l3[2] == 1) or \
    (l1[0] == 1 and l2[0] == 1 and l3[0] == 1) or \
    (l1[1] == 1 and l2[1] == 1 and l3[1] == 1) or \
    (l1[2] == 1 and l2[2] == 1 and l3[2] == 1) or \
    (l1[0] == 1 and l2[1] == 1 and l3[2] == 1) or \
    (l1[2] == 1 and l2[1] == 1 and l3[0] == 1):
    won_first = True

elif (l1[0] == 2 and l1[1] == 2 and l1[2] == 2) or \
    (l2[0] == 2 and l2[1] == 2 and l2[2] == 2) or \
    (l3[0] == 2 and l3[1] == 2 and l3[2] == 2) or \
    (l1[0] == 2 and l2[0] == 2 and l3[0] == 2) or \
    (l1[1] == 2 and l2[1] == 2 and l3[1] == 2) or \
    (l1[2] == 2 and l2[2] == 2 and l3[2] == 2) or \
    (l1[0] == 2 and l2[1] == 2 and l3[2] == 2) or \
    (l1[2] == 2 and l2[1] == 2 and l3[0] == 2):
    won_second = True
else:
    draw = True

if won_first:
    print('First player won')
elif won_second:
    print('Second player won')
elif draw:
    print('Draw!')

