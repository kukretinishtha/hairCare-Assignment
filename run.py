from preprocessing import read_dataset 
from preprocessing import get_Hair_care_dataset_with_quantity_and_volume_by_title
from preprocessing import convert_to_numeric_data, binning_the_data
from preprocessing import drop_na, write_file_to_csv_with_filename
from graphs import plot_distribution
from model import k_means_clustering, labelling_target_cluster
file_path = 'Hair_Care_dataset.xlsx'
result_file = "Labeled_Hair_care_dataset.csv"

# Read the dataset
Hair_care_dataset = read_dataset(file_path)
# Get volume and Quantity from Dataset
result = get_Hair_care_dataset_with_quantity_and_volume_by_title(Hair_care_dataset)
# Convert Dataset to numeric format
result = convert_to_numeric_data(result)
# Printing the Binned Dataset
binning_the_data(result)
# Drop na values from dataset
clustering_hair_care_data = drop_na(result, ["Quantity","Volume","SalePrice"])
# Plotting the Volume and Quantity Distribution
plot_distribution(result, "Volume", "Volume_Distribution")
plot_distribution(result, "Quantity", "Quantity_Distribution")
# Applying K-means clustering
result = k_means_clustering(clustering_hair_care_data)
# Labelling the clustered data
result = labelling_target_cluster(clustering_hair_care_data)
# Write the labelled data into csv file
write_file_to_csv_with_filename(result,result_file)