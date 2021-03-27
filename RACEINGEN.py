# cook your dish here
for _ in range(int(input())):
        x, r, m = map(int, input().split())
        r *= 60
        m *=60
        r_m_x = r-x
        total_time = r + (r_m_x if r_m_x>0 else 0)
        if total_time <= m:
            print("YES")
        else:
            print("NO")
