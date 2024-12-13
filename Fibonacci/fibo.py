import pandas as pd
import matplotlib.pyplot as plt

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
    

if __name__ == "__main__":
    n = 20
    ints = range(1, n+1)
    df = pd.DataFrame({'n': ints, 'fibo(n)': fibos(n)})
    fig, ax = plt.subplots(facecolor='lightgray')
    df.plot(x='n', y='fibo(n)', kind='line', ax=ax, color='purple')
    df.plot(x='n', y='fibo(n)', kind='scatter', ax=ax, color='purple')
    ax.set_facecolor('lightgray')
    ax.set_clip_on(False)
    ax.set_xlabel('n')
    ax.set_xticks(range( 1, n+1, 1))
    ax.set_ylabel('fibo(n)')
    ax.set_title('Fibonacci numbers')
    plt.show()