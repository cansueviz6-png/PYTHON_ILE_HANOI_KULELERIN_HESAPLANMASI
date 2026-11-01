import matplotlib.pyplot as plt

count = 0

def hanoi(n, start, end, extra):
    global count
    if n == 0:
        return
    hanoi(n - 1, start, extra, end)
    count = count + 1
    hanoi(n - 1, extra, end, start)

n = int(input("Enter the number of disks: "))

hanoi(n, "A", "C", "B")
print("Total moves:", count)

# Graph
x = []
y = []
for i in range(1, n + 1):
    x.append(i)
    y.append(2 ** i - 1)

plt.plot(x, y, marker="o")
plt.title("Tower of Hanoi")
plt.xlabel("Number of disks")
plt.ylabel("Number of moves")
plt.show()
