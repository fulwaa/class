class oddoreven:
    def odev(self, a):
        if a % 2 == 0:
            print("EVEN")

        else:
            print("ODD")


obj = oddoreven()
print(
    """choose an option
      1 repeat cheching with another another one
      2 exit"""
)

while True:
    val = int(input())
    if val == 1:
        num = int(input())
        obj.odev(num)
    elif val == 2:
        print("THANK YOU")
        break
    else:
        print("enter a valid option")
