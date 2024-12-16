from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
def fibos(n):
    numbers = [0, 1]
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        for i in range(2, n):
            numbers.append(numbers[i - 1] + numbers[i - 2])
        return numbers

x_vals = []
y_vals = []

fig, ax = plt.subplots(facecolor='lightgray')
ax.set_facecolor('lightgray')
ax.set_clip_on(False)
ax.set_xlabel('n')
ax.set_ylabel('fibo(n)')
ax.set_title('Fibonacci numbers')

index = count()

def animate(i):
    if len(x_vals) >= len(fibonacci_numbers):
        return
    else:
        x_vals.append(next(index) + 1)
        y_vals.append(fibonacci_numbers[len(x_vals)-1])

    plt.cla()
    ax.set_xticks(range(1, i + 4, 1))
    plt.plot(x_vals, y_vals, color='purple')
    plt.scatter(x_vals, y_vals, color='purple')



if __name__ == "__main__":
    n = 20
    fibonacci_numbers = fibos(n)
    anim = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.tight_layout()
    plt.show()