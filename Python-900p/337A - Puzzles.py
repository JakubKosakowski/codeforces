n, m = map(int, input().split())
tab = list(map(int, input().split()))
tab.sort()
m_v = 1000
for i in range(m - n + 1):
    temp = tab[i:i+n]
    m_v = min(m_v, (max(temp) - min(temp)))
print(m_v)
