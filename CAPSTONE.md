# Capstone Project

## Part 1
Finding clusters in data: K-means
### Learn about K-means clustering
* http://astrostatistics.psu.edu/RLectures/clustering_classification_Jessi.pdf
* https://en.wikipedia.org/wiki/K-means_clustering
* https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials
* https://vimeo.com/110060516
* https://www.youtube.com/watch?v=7_XGsbceUkY
### Get the data
* Change the data URL in the `sdss_sspp.py` file to be https://www.dropbox.com/s/m736a7j70a4p1ux/SDSSssppDR9_rerun122.fit?dl=1 and reinstall astroML to reflect the changes
* * Hint: instead of changing astroML you can also download the data to your `~/astroML_data` directory. If you make sure it is named `SDSSssppDR9_rerun122.fit` `astroML` won't try to download it again from the broken URL.
### Work with the data
1. Run the code in `Capstone_Part1.py`.
1. Change the number of clusters, and rerun, what do you get?

## Part 2
### Obtaining a new dataset yourself
1. Sign up for an account at CasJobs https://skyserver.sdss.org/CasJobs/jobdetails.aspx?id=28881961
1. Go to the query tab. Submit your own query for data by using the code in the appendix of this readme
1. Go to the download tab. Download your data (select the fit format) to PythonAnywhere
 1. On PythonAnywhere, change directories into the astroML_data directory
 1. run wget on the link to your dataset (unsure what wget is? run `man wget` to find out). Make sure to remove your username from the file name and rename it so that it is named `sgSDSSimagingSample.fit`. This will ensure instead of downloading the data from a remote link which doesn't work, `astroML` will automatically use the data you have just downloaded.
### Working with your new data
1. Run the code in `Capstone_Part2.py`
1. Modify the code from `Capstone_Part1.py` to find clusters in the new data in the galaxies and the stars.
## Part 3
### K-Nearest-Neighbor classifier
Read about K-Nearest-Neighbor classifiers
* http://astrostatistics.psu.edu/RLectures/clustering_classification_Jessi.pdf
* https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
* https://www.youtube.com/watch?v=UqYde-LULfs
### Get the data
As you did in **Part 1**either download directly to astroML_data or updated the link of the dataset in rrlyrae_mags.py to be https://www.dropbox.com/s/q2nw3jtekwjvo6c/RRLyrae.fit?dl=1 and reinstall astroML


### Work with the data
1. Run the code in `Capstone_Part3.py`.
1. Change the number of clusters, and rerun, what do you get?
## Part 4
How to choose what method to use: http://peekaboo-vision.blogspot.com/2013/01/machine-learning-cheat-sheet-for-scikit.html
* Pick to work with either astronomy and stellar data, solar flare data, or satellite imagery data. Obtain your dataset, adn then pick either K-Nearest-Neighbors or K-Means to divide it into categories. What categories did you come up with? Are you able to spot patterns. Write up your results. 


# Appendix:
The query on the SDSS server to get the data for **Part 2** is as follows:
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
The query on the SDSS server to get the data for `Problem1_Testing.py` is as follows:
```
SELECT                                                                                                                                                                                                                                                                          
     G.ra, G.dec, S.mjd, S.plate, S.fiberID,                                                                                                                                                                                                                                  
     S.z, S.zErr, S.rChi2, S.velDisp, S.velDispErr,                                                                                                                                                                                                                
     G.extinction_r, G.petroMag_r, G.psfMag_r, G.psfMagErr_r,                                                                                                                                                                                                                      
     G.modelMag_u, modelMagErr_u, G.modelMag_g, modelMagErr_g,                                                                                                                                                                                                                     
     G.modelMag_r, modelMagErr_r, G.modelMag_i, modelMagErr_i,                                                                                                                                                                                                                     
     G.modelMag_z, modelMagErr_z, G.petroR50_r, G.petroR90_r,                                                                                                                                                                   
     GSL.nii_6584_flux, GSL.nii_6584_flux_err, GSL.h_alpha_flux,                                                                                                                                                                                                                   
     GSL.h_alpha_flux_err, GSL.oiii_5007_flux, GSL.oiii_5007_flux_err,                                                                                                                                                                                                             
     GSL.h_beta_flux, GSL.h_beta_flux_err, GSL.h_delta_flux,                                                                                                                                                                                                                       
     GSL.h_delta_flux_err, GSX.d4000, GSX.d4000_err, GSE.bptclass,                                                                                                                                                                                                                 
     GSE.lgm_tot_p50, GSE.sfr_tot_p50, G.objID, GSI.specObjID                                                                                                                                                                                                                      
INTO mydb.SDSSspecgalsDR8 FROM SpecObj S CROSS APPLY                                                                                                                                                                                                                            
     dbo.fGetNearestObjEQ(S.ra, S.dec, 0.06) N, Galaxy G,                                                                                                                                                                                                                          
     GalSpecInfo GSI, GalSpecLine GSL, GalSpecIndx GSX, GalSpecExtra GSE                                                                                                                                                                                                           
WHERE N.objID = G.objID                                                                                                                                                                                                                                                         
     AND GSI.specObjID = S.specObjID                                                                                                                                                                                                                                               
     AND GSL.specObjID = S.specObjID                                                                                                                                                                                                                                               
     AND GSX.specObjID = S.specObjID                                                                                                                                                                                                                                               
     AND GSE.specObjID = S.specObjID                                                                                                                                                                                                   
     AND (G.petroMag_r > 10 AND G.petroMag_r < 18)                                                                                                                                                                                                                                 
     AND (G.modelMag_u-G.modelMag_r) > 0                                                                                                                                                                                                                                           
     AND (G.modelMag_u-G.modelMag_r) < 6                                                                                                                                                                                                                                           
     AND (modelMag_u > 10 AND modelMag_u < 25)                                                                                                                                                                                                                                     
     AND (modelMag_g > 10 AND modelMag_g < 25)                                                                                                                                                                                                                                     
     AND (modelMag_r > 10 AND modelMag_r < 25)                                                                                                                                                                                                                                     
     AND (modelMag_i > 10 AND modelMag_i < 25)                                                                                                                                                                                                                                     
     AND (modelMag_z > 10 AND modelMag_z < 25)                                                                                                                                                                                                                                     
     AND S.rChi2 < 2                                                                                                                                                                                                                                                               
     AND (S.zErr > 0 AND S.zErr < 0.01)                                                                                                                                                                                                                                            
     AND S.z > 0.02
```
