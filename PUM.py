n = int(input()) * 4

for i in range(1,n):
    if i % 4 == 0:
        print("PUM",end="\n")
        continue
    print(i,end=' ')
if n % 4 == 0:
    print("PUM")



a=1
for i in range(int(input())):
    print(f"{a} {a+1} {a+2} PUM")
    a+=4