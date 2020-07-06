N = int(input())
S = [input() for i in range(N)]
AC, WA, TLE, RE = 0, 0, 0, 0
AC = S.count("AC")
WA = S.count("WA")
TLE = S.count("TLE")
RE = S.count("RE")
print('AC x {}'.format(AC))
print('WA x {}'.format(WA))
print('TLE x {}'.format(TLE))
print('RE x {}'.format(RE))
