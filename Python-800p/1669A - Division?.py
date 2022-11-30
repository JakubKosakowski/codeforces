t = int(input())
for i in range(t):
    rating = int(input())
    print("Division 1" if rating >= 1900
           else "Division 2" if rating <= 1899 and rating >= 1600
           else "Division 3" if rating <= 1599 and rating >= 1400
           else "Division 4")
