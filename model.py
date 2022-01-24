from sklearn.cluster import KMeans 
import matplotlib.pyplot as mtp 

def k_means_clustering(data_in_numpy):
    wcss_list= [] 
    for i in range(1, 11):  
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state= 42)  
        kmeans.fit(data_in_numpy) 
        wcss_list.append((kmeans.inertia_)) 
    mtp.plot(range(1, 11), wcss_list)  
    mtp.title('The Elobw Method Graph')  
    mtp.xlabel('Number of clusters(k)')  
    mtp.ylabel('wcss_list')
    mtp.savefig("Elbow Graph", facecolor= 'w', bbox_inches="tight",pad_inches=0.3, transparent=True)

def labelling_target_cluster(dataset, number_of_cluster=4):
    kmeans = KMeans(n_clusters=number_of_cluster, init='k-means++', random_state= 4)
    kmeans.fit(dataset)
    labels = kmeans.fit_predict(dataset).tolist()
    dataset['labels'] = labels
    return dataset