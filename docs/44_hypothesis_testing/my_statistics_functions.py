import matplotlib.pyplot as plt

def draw_curation_time_histogram(data, description):
    fig, ax = plt.subplots()
    ax.hist(data, bins=10)
    ax.set_title('Curation time of ' + str(len(data)) + ' ' + description)
    ax.set_ylabel("count")
    ax.set_xlabel("Curation time / days")
    plt.show()


test_data = [1,1, 3,3, 5,6,7, 9,9]

draw_curation_time_histogram(test_data, "examples")


