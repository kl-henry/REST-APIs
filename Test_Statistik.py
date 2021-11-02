import numpy as np
from matplotlib import pyplot as plt

max_temp = ['15.55', '14.04', '15.18', '21.18', '24.44', '15.18', '24.18', '18.78', '15.47',
            '15.57', '21.26', '18.47', '19.44']
curr_date = [u'28.Aug.2021', u'29.Aug.2021', u'30.Aug.2021', u'31.Aug.2021', u'02.Sep.2021',
             u'03.Sep.2021', u'04.Sep.2021', u'05.Sep.2021', u'06.Sep.2021', u'07.Sep.2021',
             u'09.Sep.2021', u'10.Sep.2021', u'11.Sep.2021']

min_temp = ['13.22', '12.72', '12.81', '17.25', '21.47', '8.45', '19.96', '14.27', '11.23', '11.66', '16.74', '15.5',
            '16.41']


def call_graph(max_temp_np=None, min_temp_np=None, curr_date_np=None):
    fig, (ax1, ax3) = plt.subplots(2, 1)
    fig.suptitle('Min./Max Temperatur')
    fig.supxlabel('Datum')
    fig.supylabel('Temperatur °C')

    ax1.grid()
    ax3.grid()
    # print(max_temp_np, type(max_temp))
    # print(curr_date_np, type(curr_date))

    max_temp_np = np.array(max_temp_np)
    min_temp_np = np.array(min_temp_np)
    curr_date_np = np.array(curr_date_np)

    max_temp_array = np.array(max_temp)
    max_temp_array = max_temp_array.astype(float)
    max_temp_array = max_temp_array.astype(int)
    max_temp_array.sort()
    max_temp_array = np.unique(max_temp_array)
    # print("max_temp_array: ", max_temp_array)
    min_value = min(max_temp_array) - 1
    max_value = max(max_temp_array) + 1
    # print("max_temp_array, min max: ", min_value, max_value)
    y_ticks = np.linspace(min_value, max_value, max_value - min_value, endpoint=False, dtype=int)
    # print("y_ticks: ", y_ticks)
    ax1.set_yticks(y_ticks)
    ax1.set_yticklabels(labels=y_ticks, fontsize=7)

    # print(max_temp_np, type(max_temp_np))
    # print(curr_date_np, type(curr_date_np))

    ax1.plot(curr_date_np, max_temp_np.astype(float), 'bo-')
    ax1.set_xticks(curr_date_np)
    ax1.set_xticklabels(labels=curr_date_np, fontsize=5, rotation=45)

    # print("ax3: ", curr_date_np, min_temp_np.astype(float))
    ax3.plot(curr_date_np, max_temp_np.astype(float))
    ax3.plot(curr_date_np, min_temp_np.astype(float))
    ax3.set_xticks(curr_date_np)
    ax3.set_xticklabels(labels=curr_date_np, fontsize=5, rotation=45)
    temperature = min_temp + max_temp
    temperature = np.array(temperature)
    temperature = temperature.astype(float)
    temp_array = temperature.astype(int)
    temp_array.sort()
    temp_array = np.unique(temp_array)
    min_value = min(temp_array) - 1
    max_value = max(temp_array) + 1

    # print("max_temp_array, min max: ", min_value, max_value)
    y_ticks = np.linspace(min_value, max_value, max_value - min_value, endpoint=False, dtype=int)
    print("y_ticks: ", y_ticks)
    ax3.set_yticks(y_ticks)
    ax3.set_yticklabels(labels=y_ticks, fontsize=7)
    plt.ylim(min_value, max_value)
    print("temperatur_gesamt: ", temp_array)



if __name__ == "__main__":
    call_graph(max_temp, min_temp, curr_date)
    plt.show()
