def check(s):
    for x in range(len(s)):
        if s[x] == s[len(s)-(x+1)]:
            pass
        else:
            return False
    return True

ss = input()

if check(ss):
    print("1")
else:
    print("0")
