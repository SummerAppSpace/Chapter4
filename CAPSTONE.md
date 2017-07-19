# Capstone Project
## Update your `git`
Note if you've already created a git repository in your own github following the instructions in the textbook prior to the release of this file, you will have to add this git repository as a new remote and pull the code updates and CAPSTONE.md files. Do that by running
```
git remote add chapter4 git@github.com:SummerAppSpace/Chapter4.git
git pull chapter4 master
```
## Part 1
Finding clusters in data: K-means
### Learn about K-means clustering
* http://astrostatistics.psu.edu/RLectures/clustering_classification_Jessi.pdf
* https://en.wikipedia.org/wiki/K-means_clustering
* https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials
* https://vimeo.com/110060516
* https://www.youtube.com/watch?v=7_XGsbceUkY
### Work with the data<sup>1</sup>
1. Run the code in `Capstone_Part1.py`
1. Change the number of clusters, and rerun, what do you get?

<sup>1</sup> Note: if you have any problems with the data not being accessible, change the data URL in the `sdss_sspp.py` file to be https://www.dropbox.com/s/m736a7j70a4p1ux/SDSSssppDR9_rerun122.fit?dl=1 and reinstall astroML to reflect the changes OR instead of changing astroML you can also download the data to your `~/astroML_data` directory. If you make sure it is named `SDSSssppDR9_rerun122.fit` `astroML` won't try to download it again from the broken URL.

## Part 2
### Obtaining a new dataset yourself
1. Sign up for an account at http://portal.sciserver.org/login-portal/Account/Register
1. Login at CasJobs https://skyserver.sdss.org/CasJobs/jobdetails.aspx?id=28881961
1. Go to the query tab. Submit your own query for data by using the code in the appendix of this file. Make sure you change contexts in the dropdown to `DR12`
1. Check on the progress of your query at http://skyserver.sdss.org/CasJobs/ViewJobs.aspx It will changed to Finished when successful. If there is a failure, double check that your context was correct.
1. Go to the MyDb tab. Click on the name of your database, SDSSImagingSample. Click on Download. Select the Fit format and click Go. When the data is ready it will appear on: http://skyserver.sdss.org/CasJobs/output.aspx
1. Download your data (select the fit format) to PythonAnywhere: 
 1. On the Output tab right click Download next to your data, and Copy Link Location.
 1. On PythonAnywhere, change directories into the astroML_data directory
 1. run wget on the link to your dataset (unsure what wget is? run `man wget` to find out). Make sure to rename the file so that it is named `sgSDSSimagingSample.fit`. This will ensure instead of downloading the data from a remote link which doesn't work, `astroML` will automatically use the data you have just downloaded.
### Working with your new data
1. Run the code in `Capstone_Part2.py`
1. Modify the code from `Capstone_Part1.py` to find clusters in the new data in the galaxies and the stars.
## Part 3
### K-Nearest-Neighbor classifier
Read about K-Nearest-Neighbor classifiers
* http://astrostatistics.psu.edu/RLectures/clustering_classification_Jessi.pdf
* https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
* https://www.youtube.com/watch?v=UqYde-LULfs
### Work with the data<sup>2</sup>
1. Run the code in `Capstone_Part3.py`.
1. Change the number of neighbors used, and rerun, what do you get? What changes?

<sup>2</sup>If you have any problems reaching the data, as you did in **Part 1** either download directly to astroML_data or updated the link of the dataset in rrlyrae_mags.py to be https://www.dropbox.com/s/q2nw3jtekwjvo6c/RRLyrae.fit?dl=1 and https://www.dropbox.com/s/n8trp77urpbg01b/stripe82calibStars_v2.6.dat.gz?dl=1 respectively and reinstall astroML
## Part 4
Pick one of the queries in the appendix and modify it slightly. Perhaps select for a different (recommended: smaller to ensure the output is smaller) range for one of the values. Look up what that physically means. Then, once you have your new dataset, save the old one under a new name in `~/astroML_data`, your new dataset under the same name as the old one previously had, and this will let `astroML` use your new dataset instead for the same problem without further changes. Compare the outputs and your results between the different datasets.
## Part 5
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
        WHERE
            --- 10x2 sq.deg.
          p.ra > 0.0 and p.ra < 10.0 and p.dec > -1 and p.dec < 1
            --- resolved and unresolved sources
          and (p.type = 3 OR p.type = 6) and
            --- '4295229440' is magic code for no
            --- DEBLENDED_AS_MOVING or SATURATED objects
          (p.flags & '4295229440') = 0 and
            --- PRIMARY objects only, which implies
            --- !BRIGHT && (!BLENDED || NODEBLEND || nchild == 0)]
          p.mode = 1 and
            --- adopted faint limit (same as about SDSS limit)
          p.modelMag_r < 22.5
        --- the end of query
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
