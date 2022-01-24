import matplotlib.pyplot as mtp 

def plot_distribution(dataframe, column_name, distribution_name):
    dataframe.hist(column=column_name)
    mtp.savefig(distribution_name, facecolor= 'w', bbox_inches="tight",pad_inches=0.3, transparent=True)
    return "Distribution has been saved succesfully"