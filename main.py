def solve(N, M, A, B):
    o = sorted(zip(A, B))
    skill = M

    for a, b in o:
        if skill >= a:
            skill += b
        else:
            break
    return skill

N, M = map(int, input().split())
A = list(map(int, input().split()))[:N]
B = list(map(int, input().split()))[:N] 
print(solve(N, M, A, B))