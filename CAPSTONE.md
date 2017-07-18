# Capstone Project

## Part 1
Finding clusters in data: K-means
### Learn about K-means clustering
* https://en.wikipedia.org/wiki/K-means_clustering
* https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials
* https://vimeo.com/110060516
## Get the data
Change the data URL in the `sdss_sspp.py` file to be https://www.dropbox.com/s/m736a7j70a4p1ux/SDSSssppDR9_rerun122.fit?dl=1 and reinstall astroML to reflect the changes

## Work with the data
1. Run the code in `Capstone_Part1.py`.
1. Change the number of clusters, and rerun, what do you get?

## Part 2
### Obtaining a new dataset yourself
1. Sign up for an account at CasJobs https://skyserver.sdss.org/CasJobs/jobdetails.aspx?id=28881961
1. Submit your own query for data in the following way:
1. Download your data
 1. On python anywhere, change directories into the astroML_data directory, in your home directory
 1. run wget on the link to your dataset
### Working with your new data
1. Run the code in `Capstone_Part2.py`
1. Modify the code from `Capstone_Part1.py` to find clusters in the new data in the galaxies and the stars.
