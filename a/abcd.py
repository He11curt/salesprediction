def getres(number):
    even=[]
    str1=""
    for i in range(len(number)):
        if(int(i)%2==0):
            even.append(number[i])
    for i in range(len(number)):
        if(int(i)%2!=0):
            even.append(number[i])
    for i in even:
        str1+=i
    print(str1)
    pass
def main():
    n=int(input())
    for i in range(n):
        str2=input()
        getres(str2)
main()
