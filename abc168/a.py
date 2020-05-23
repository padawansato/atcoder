n = input()
first = int(n[-1:])
hon = [2,
       4,
       5,
       7,
       9
       ]
pon = [0,
       1,
       6,
       8
       ]
bon = [3]


if first in hon:
    print("hon")
elif first in pon:
    print("pon")
else:
    print("bon")

# if int((str(n)[-1:])) in hon:
#     print("hon")
# elif int(str(n)[-1:]) in pon:
#     print("pon")
# else:
#     print("bon")
