# vb-auto-accidents

## Abstract
Virginia Beach has had a rising amount of tourists, as travel has returned to pre-pandemic levels. With this onslaught of new drivers, accident rates have also risen as a result. In order to help spread awareness and safety for the tourists and residents, this paper aims to identify which roads/intersections in Virginia Beach are unsafe and when/how they are dangerous. We developed a clustering model of the Geo-locations of accidents to map out the locations of where they took place and to extrapolate information about them. Our analysis identifies the most dangerous intersection by taking into account the number of accidents that have occured at those locations, as well as other metrics. Through several unsupervised clustering methods (DBSCAN, KMeans, and Agglomerative Clustering), we identified a few roads where a large portion of accidents take place: Lynnhaven Parkway, Independence Boulevard, 24th Street, Holland Road, Virginia Beach Boulevard, Indian River Road, and Princess Anne Road. On average, 284 accidents have taken place on each of these roads, with a large portion of them occuring on the days Thursday, Friday, and Saturday.

## Running the Notebooks
To run the notebooks, first create a virtual environment
```
python3 -m venv env
```

Then, depending on if you are Windows or Mac, activate your virtual environment with the following for Mac
```
source env/bin/activate
```
or the following for Windows
```
.\env\Scripts\activate
```

Then, install the needed requirements with
```
pip install -r requirements.txt
```

Finally, start up Jupyter Lab by running
```
jupyter-lab
```
