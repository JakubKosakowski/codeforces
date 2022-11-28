t = int(input())
for i in range(t):
    s = input()
    if not("0" in s):
        print("NET")
    elif s.count("0") == 1 and s.count("1") == 1:
        print("DA")
    else:
        a_flag = False
        b_flag = True
        while(True):
            if "10" in s:
                if not a_flag:
                    a_flag = True
                    b_flag = False
                elif not b_flag:
                    a_flag = False
                    b_flag = True
                s = s.replace("10","",1)
            elif "01" in s:
                if not a_flag:
                    a_flag = True
                    b_flag = False
                elif not b_flag:
                    a_flag = False
                    b_flag = True
                s = s.replace("01","",1)
            else:
                break
        if a_flag:
            print("DA")
        else:
            print("NET")
