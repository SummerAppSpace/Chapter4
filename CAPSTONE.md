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
```
SELECT
          round(p.ra,6) as ra, round(p.dec,6) as dec,
          p.run,                              --- comments are preceded by ---
          round(p.extinction_r,3) as rExtSFD, --- r band extinction from SFD
          round(p.modelMag_u,3) as uRaw,      --- ISM-uncorrected model mags
          round(p.modelMag_g,3) as gRaw,      --- rounding up model magnitudes
          round(p.modelMag_r,3) as rRaw,
          round(p.modelMag_i,3) as iRaw,
          round(p.modelMag_z,3) as zRaw,
          round(p.modelMagErr_u,3) as uErr,   --- errors are important!
          round(p.modelMagErr_g,3) as gErr,
          round(p.modelMagErr_r,3) as rErr,
          round(p.modelMagErr_i,3) as iErr,
          round(p.modelMagErr_z,3) as zErr,
          round(p.psfMag_u,3) as psfRaw,      --- psf magnitudes
          round(p.psfMag_g,3) as psfRaw,
          round(p.psfMag_r,3) as psfRaw,
          round(p.psfMag_i,3) as psfRaw,
          round(p.psfMag_z,3) as psfRaw,
          round(p.psfMagErr_u,3) as psfuErr,
          round(p.psfMagErr_g,3) as psfgErr,
          round(p.psfMagErr_r,3) as psfrErr,
          round(p.psfMagErr_i,3) as psfiErr,
          round(p.psfMagErr_z,3) as psfzErr,
          p.type,                   --- tells if a source is resolved or not
          (case when (p.flags & '16') = 0 then 1 else 0 end) as ISOLATED
        INTO mydb.SDSSimagingSample
        FROM PhotoTag p

```
1. Download your data
 1. On python anywhere, change directories into the astroML_data directory, in your home directory
 1. run wget on the link to your dataset. Make sure to remove your username from the file name so that it is `sgSDSSimagingSample.fit`. Then, instead of downloading the data from a remote link which doesn't work, `astroML` will automatically use the data you have downloaded.
### Working with your new data
1. Run the code in `Capstone_Part2.py`
1. Modify the code from `Capstone_Part1.py` to find clusters in the new data in the galaxies and the stars.
