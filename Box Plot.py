# Plot box plot of a column in the dataset
def plot_box_plot(dataset, column):
    dataset[column].plot.box()
    plt.ylabel("Values")
    plt.title("Box Plot")
    plt.show()

# Example usage:
plot_box_plot(dataset, 'column_name')
