import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {str(i + 1): input().strip() for i in range(N)}
inv_pokedex = {v: k for k, v in pokedex.items()}

for _ in range(M):
    key = input().strip()
    if key.isdecimal():
        print(pokedex[key])
    else:
        print(inv_pokedex[key])
