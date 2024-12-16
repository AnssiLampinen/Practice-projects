import matplotlib.pyplot as plt


n = 20

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

x_vals = range(1, n+1)
y_vals = fibos(n)

fig, ax = plt.subplots(facecolor='lightgray')
ax.set_facecolor('lightgray')
ax.set_clip_on(False)
ax.set_xlabel('n')
ax.set_ylabel('fibo(n)')
ax.set_title('Fibonacci numbers')
ax.set_xticks(range(1, 21, 1))
annotation = ax.annotate(
    text='Fibonacci numbers',
    xy=(0, 0),
    xytext=(15, 15),
    bbox={'boxstyle': 'round', 'facecolor': 'white', 'alpha': 0.5},
    arrowprops={'arrowstyle': '->', 'color': 'black'}
    )
annotation.set_visible(False)

scatter = plt.scatter(x_vals, y_vals, color='purple')
line = plt.plot(x_vals, y_vals, color='purple')

subscript_map = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"
    }

trans = str.maketrans(
    ''.join(subscript_map.keys()),
    ''.join(subscript_map.values()))

def motion_hover(event):
    annotation_visible = annotation.get_visible()
    if event.inaxes == ax:
        is_datapoint, index = scatter.contains(event)
        if is_datapoint:
            data_point = scatter.get_offsets()[index['ind'][0]]
            annotation.xy = data_point
            annotation.xyann = (data_point[0] - 3 + (10 - data_point[0])/3, data_point[1] + (2000 - data_point[1])/5)
            text_label = f'F{str(int(data_point[0])).translate(trans)} = {int(data_point[1])}'
            annotation.set_text(text_label)
            annotation.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if annotation_visible:
                annotation.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", motion_hover)

if __name__ == "__main__":
    plt.tight_layout()
    plt.show()
