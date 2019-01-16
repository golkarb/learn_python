dates=[1990, 1991, 1992] # dates is a list
N=len(dates)

for i in range(N):
    print(dates[i])

print("\n=========================\n")

for x in dates:
    print(x)

print("\n=========================\n")

for i,x in enumerate(dates):
    print("date",i,"is", x)
