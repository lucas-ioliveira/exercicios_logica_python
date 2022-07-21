print(f"Digite dois números: ")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print(f"CRESCENTE")
    else:
        print(f"DECRESCENTE")

    print("Digite outros dois valores: ")
    x = int(input())
    y = int(input())
