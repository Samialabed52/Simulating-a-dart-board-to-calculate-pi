import random as rand
import seaborn as sns
import pandas as pd
import matplotlib as mpl


def get_pi(N)->[float]:
    n = 0
    x_arr = []
    y_arr = []
    in_range = []
        
    for _ in range(N):
        x = rand.uniform(0,1)
        y = rand.uniform(0,1)
        
        radius = (x ** 2) + (y ** 2)
    
        if radius <= 1:
            n += 1
            in_range.append(1)
        else:
            in_range.append(0)
            
        x_arr.append(x)
        y_arr.append(y)
    
    in_data = pd.DataFrame({'x': x_arr, 'y': y_arr, 'in range': in_range})

    
    plot1 = sns.scatterplot(x = 'x', y = 'y', hue = 'in range', data = in_data)   
    plot = plot1.get_figure()
    plot.savefig(f'plot{N}')
    plot.clear()
    
    pi = 4 * (n / N)
    print(pi)
    return pi

pi_list = []

ten_pi = get_pi(10)
pi_list.append(ten_pi)

hund_pi = get_pi(100)
pi_list.append(hund_pi)

thous_pi = get_pi(1_000)
pi_list.append(thous_pi)

ten_thous_pi = get_pi(10_000)
pi_list.append(ten_thous_pi)

hund_thous_pi = get_pi(100_000)
pi_list.append(hund_thous_pi)

N_vals = [10, 100, 1000, 10_000, 100_000]

title = 'Values of pi for different arrays of size N'

sns.set_style('whitegrid')

plot = sns.barplot(x = N_vals, y = pi_list, palette = 'bright')

plot.set_title(title)
plot.set(xlabel = 'N array sizes', ylabel = 'Pi values')

for bar, pi_val in zip(plot.patches, pi_list):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{pi_val:.5}'
    plot.text(text_x, text_y, text, fontsize = 11, ha = 'center', va = 'bottom')

plot1 = plot.get_figure()
plot1.savefig('pi_values')