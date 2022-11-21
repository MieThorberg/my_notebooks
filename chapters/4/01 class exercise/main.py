import numpy as np
import matplotlib.pyplot as plt

filename = '../../../../data/befkbhalderstatkode.csv'
dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}

# method to get the sum of all people living in a neighbourhood
def number_of_people_per_neighb(neighb, mask):
    all_people_in_given_neighb = dd[mask & (dd[:, 1] == neighb)]
    sum_of_people = all_people_in_given_neighb[:, 4].sum()
    return sum_of_people

# print amount of people living in the neighbourhood
def amount_of_people_from_neighb():
    mask = (dd[:, 0] == 2015)
    peoples = [number_of_people_per_neighb(n, mask) for n in neighb.keys()]
    i = 0
    for n in neighb.values():
        print(str(peoples[i]) + " " + str(n))
        i += 1

# print amount of people above 65 years living in the neighbourhood
def people_above_65():
    mask = (dd[:,0] == 2015) & (dd[:,2] > 65)
    people_sum_in_neighb = [number_of_people_per_neighb(n, mask) for n in neighb.keys()]
    amount = 0
    for people_sum in people_sum_in_neighb:
        amount += people_sum
    print("The total of people above 65 years is: " + str(amount))

# print amount of people above 65 years and from other nordic countries (not dk)
def people_above_65_from_nordic_countries():
    nordic_countries = [5101,5104,5106,5110,5120]
    amount = 0
    for country in nordic_countries:
        mask = (dd[:, 0] == 2015) & (dd[:, 2] > 65) & (dd[:,3] == country)
        people_sum = dd[mask][0:,4].sum()
        amount += people_sum
    print("The total of people above 65 years and from a nordic county is: " + str(amount))

# create a line plot showing the changes of people
# in vesterbro and østerbro from 1992 to 2015
def line_plot():
    years = [1992+i for i in range(2016-1992)]
    v_peoples = [number_of_people_per_neighb(4, ((dd[:, 0] == year) & (dd[:, 2] > 65))) for year in years]
    o_peoples = [number_of_people_per_neighb(2, ((dd[:, 0] == year) & (dd[:, 2] > 65))) for year in years]
    plt.plot(years, v_peoples,  label = "Vesterbro")
    plt.plot(years, o_peoples, label = "Østerbro")
    plt.legend()
    plt.show()
line_plot()
def get_plot_of_people_in_neighb():
    # make a dictionary with neighbour with amount of peoples
    neighb_sorted = {}
    mask = (dd[:, 0] == 2015)
    peoples = [number_of_people_per_neighb(n, mask) for n in neighb.keys()]
    i = 0
    for n in neighb.values():
        neighb_sorted[n] = peoples[i]
        i += 1

    neighb_sorted
    # sort
    sorted_value_index = np.argsort(neighb_sorted.values())
    dict_keys = list(neighb_sorted.keys())
    dict_keys

    l = {
        dict_keys[i]: sorted(neighb_sorted.values())[i]
        for i in range(len(neighb_sorted))
    }
    l

    # plot bar
    labels = [label for label in neighb.values()]
    x = np.arange(len(labels))
    width = 0.35
    values = [i for i in l.values()]
    plt.bar(labels, values, width=0.5, align='center')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    plt.ylabel("People")
    plt.xlabel("Neighbourhood")
    plt.title("People in neighbourhood")
    plt.show()
