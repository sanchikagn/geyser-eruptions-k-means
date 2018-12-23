# geyser-eruptions-k-means

### What are geysers?
A natural geyser is a spring that intermittently discharges hot water via the surface of the Earth which extracts heat from the Earth. Geysers are resulted from the heating of ground water by shallow bodies of magma which are usually associated with historic volcanic activities involved areas around the globe. This discharging/spouting action is caused by the release of pressure from the boiling water beneath a geyser in a considerable depth with a narrow dimension. 

This pressure is released to the atmosphere through a conduit from the origin point to the Earth’s surface. Then the water at the depth exceeds its boiling point and flashes causing more water through the conduit while reducing the pressure further.

### The Dataset
The scientists, geologists and government authorities have the interest and have engaged in the observations and analysis of the geysers and eruptions throughout several decades. Old Faithful is one of the most studied and observed geysers although it is not the largest geyser active currently. In this approach, Old Faithful Geyser data is being analyzed with a machine learning approach to support the observations for predicting future behavior of not only geysers, but also the Earth.

•	The dataset of Old Faithful that has been occupied here was obtained from:

https://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat

https://app.quadstat.net/dataset/r-dataset-faithful

•	The dataset contains waiting time between two consecutive eruptions (in minutes) and the duration of the eruption (in minutes) for the Old Faithful geyser.

•	There are 272 observations of eruptions occurred in Old Faithful.

### K-means Clustering
K-Means is a clustering algorithm which is rapidly used from the beginning of Machine Learning era to facilitate clustering analysis of data. It is a centroid-based, iterative algorithm that partitions data into K number of non-overlapping subgroups. This algorithm is randomly initialized, and then it iterates while assigning centroids, clustering points around centroids and comparing each data point with every centroid to find the difference. This difference is measured with Euclidean distance between considered points in the calculation.

### Applying K-means to geyser eruptions
This implementation is performed using Python programming language and related libraries to achieve the task. All 272 observations from the source have been taken into account for the purpose.

The value that has been assigned for K is 2 to perform K-means algorithm, and two clusters have been derived from the standardized data. The standardizing of data means containing data with a zero mean and standard deviation of one which is recommended because the features might not be in the same measurement units.

The two clusters in data interprets that there are two series of eruptions in Old Faithful geyser; eruptions with short intervals and eruptions with long intervals (more than 3 minutes). The eruptions with long intervals last longer than short interval eruptions, because longer eruptions require more effort than short interval discharges. Furthermore, the geyser is having an increasing number of long eruptions than shorter eruptions. 

According to the above details, it can be assumed that Old Faithful geyser has varying behavior upon eruption in different situations. These conditions including atmospheric temperature, availability of water, wind speed, depth of the conduit, distant earthquakes should be analyzed further for authenticating those variations. The approach that is implemented in this scenario with K-means could provide predictions for future eruptions in terms of their duration and waiting time.
