import timeit

first_case = '''
def miss(a,b):
    if (a/b) > 0.5:
        return 2
    else:
        return 1
        
miss(4,5)
'''

second_case = '''
def miss(a,b):
    if (a/b) < 0.5:
        return 1
    else:
        return 2
        
        
miss(4,5)
'''


for i in range(0, 10):
    repetitions = 10000000
    time1 = timeit.timeit(stmt=first_case, number=repetitions), "without"
    time2 = timeit.timeit(stmt=second_case, number=repetitions), "with"

    best, worst = (time1, time2) if time1 < time2 else (time2, time1)

    print(f"Best function {best[1]} cash miss:", best[0])
    print(f"Worst function {worst[1]} cash miss:", worst[0])
    best = best[0]
    worst = worst[0]
    print(f"Delta {worst} - {best} = ",  worst-best)
    print("Boost(in %):", (worst-best)/best * 100)
    print()