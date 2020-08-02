T = int(input())
while(T):
    basic_salary = int(input())
    if(basic_salary < 1500):
        hra = 0.1 * basic_salary
        da = 0.90 * basic_salary
        print(basic_salary+hra+da)
    else:
        hra = 500
        da = 0.98*basic_salary
        print(basic_salary+hra+da)
    T -=1