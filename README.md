# **ih_datamadpt0420_project_m2**

![Image](https://res.cloudinary.com/dute7e5ne/image/upload/v1597084551/project02_banner_02_salpov.jpg)

#### :pushpin: **Base Dataset**

Dataset for this project can be downloaded [here](http://www.potacho.com/files/ironhack/diamonds_train.csv). 

In the DB there is made of the following columns:
- Geometrical measurements ['x', 'y', 'z'], with unknown units (they could be both milimeters or percentages)
- Carat: unit of mass used for gemstones and pearls. Equals 0.200gr
- Price: target measurement for the prediction model to be built in Module 3.
- Depth, Table: measurements taken in diamonds to better undestand how its geometry impact light reflexion and diamonds' beauty.
- Color, Clarity and Cut: cualitative scales stablished by experts and commonly used for the assessment of diamonds' price in the market field.

---

### :chart_with_upwards_trend: **Challenge 1** Exploratory Data Visualization Charts and Summary Statistics ###


The first challenge of this project is to build an **exploratory data analysis report** in order to gain initial insight on our **diamonds dataset**. 

The notebook is structured as follows:

- Report 1: Data exploration, cleaning and normalization with summary Statistics, including descriptive statistics (max, min, mean, standard deviation, percentiles, correlations, etc.) and data types (integer, float, boolean, string, etc.).
- Report 2: Multi-variable analysis. Looking more closely at combinations of characteristics and synthetic metrics against price.


### :paperclip: Toolkit:

The libraries used for the data visualization are the following:

- [Matplotlib](https://matplotlib.org/)
- [Pandas Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Numpy v1.18](https://numpy.org/)

---
### :chart_with_downwards_trend: **Challenge 2: Tableau Data Dashboard**

The goal of this second challenge was to build a **data dashboard** using the data and the forementioned notebooks' conclusions to help me perform better during Module 3 project (Kaggle Competition); displaying the most relevant metrics and key data points in order to get as close as possible to diamonds' price and understand the predictive model at a glance.

The dahsboard is design to best fit an 1980x1080 screen in full view. There has been also been noticed some typography compatibility problems in different internet browsers, that should be resolved in the future.

##### [DASHBOARD LINK](https://public.tableau.com/profile/lamdam#!/vizhome/IH_Project2_DIAMOND_PRICE_ANALYSIS/DIAMOND)
![Image](https://res.cloudinary.com/dute7e5ne/image/upload/v1597084540/tableau_public_r14qsx.png)

To communicate the main conclusions from the exploratory analysis, the dashboard has been divided into two main columns, with interactive filters at the left corner to be able to explored the dataset.
- The first showcases the discrete variables and their impact on price, since they are the easiest metrics to take into consideration:

    · Carat vs Price, since is the most important metric to impact the target it is at the center, showing the most relevant ranges of distribution.
    
    · Cut vs Price, cut is related to the geometrical metrics and has a linear relationship with price (the better the cut, the higher the price). The better understand the rest of metrics, the distribution of the different cut qualities is highlighted.
    
    · Color / Clarity vs Price. They are both secondary metrics to take into account and their cualitative nature makes very difficult to stablish an hierarchy. *After class presentation* it was pointed out that rapaports used in the diamonds' market are the norm to stablish an initial diamond's price, knowing it weight and cut quality.

- The second column shows the main quantitative metrics through synthetic variables:

    · Table / Depth : Both metrics are given in the dataset and the comparison between both of them have a heavy impact in the habilitiy of a diamond to create 'fire' and brilliance. Therefore, their relashionship  and its comparison with the target metric, showcases the range in which price is higher.
    
    · X/Y: this metric was created taken into account that the dataset comprises only of **round diamonds**; therefore, the lower the number, the more symmetric and better the artistry of the cut. Most numbers are very low and it is implied that there is a threshold from which the assymetry is percieved.
    
    · Volume / Weight : the volume taken into consideration is the result of **X x Y x Z**, which is the prismatic volume that encloses the diamonds.This metric is the inverse of the density of diamonds, deleting constants that are not necessary for the comparison with the target metric.


### :paperclip: Link : ###

- [Tableau Public](https://public.tableau.com/)
- [Tableau Useful tricks](https://towardsdatascience.com/5-hacky-tableau-techniques-cf3b039345ea)

--- 

### :bookmark: **Bibliography:**

- [Diamonds GIAs Grading](https://www.gia.edu/gem-education/course-diamond)
- [Diamonds Depth and Table price impact](https://beyond4cs.com/grading/depth-and-table-values/)
- [Ideal Depth and Table for diamonds](https://www.diamonds.pro/education/diamond-depth-and-table/)
- [Understanding Color Grade Scale](https://www.diamonds.pro/education/color/)
- [Diamonds Rapaport Example](http://www.dgalab.com/certificate/round.pdf)
- [Diamonds Pricing](https://www.diamonds.pro/education/diamond-prices/)
- [Understanding Clarity Grade Scale](https://www.diamonds.pro/education/clarity/)
--- 

### :book: ** Other References on Data Visualization**

- [Financial Times Visual Vocabulary](https://github.com/ft-interactive/chart-doctor/tree/master/visual-vocabulary)
- [Tableau Viz of the Day](https://public.tableau.com/es-es/gallery/?tab=viz-of-the-day&type=viz-of-the-day)
- [Introducing plotly express](https://medium.com/plotly/introducing-plotly-express-808df010143d)
- [Pandas for Data Visualization](https://towardsdatascience.com/pandas-put-away-novice-data-analyst-status-part-2-8df616d5ac7c)

---
### :love_letter: **Contact info**
linkedin.com/in/lauramielgo for inqueries.

### :hearts: **Thanks**
Big thanks to TAs, teachers and classmates for the help and support in the development of this project:

@github/potacho

@github/TheGurus

---
#### :construction: Status
Version 1.0 [01.058.2020] > Only finished Tableau Dashboard for Project presentation. Ordered reports as a homework for holidays

Version 1.0.[12.08.2020] > Reports closed and Tableau Dashboard improved after class presentation 