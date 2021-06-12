# SQLAlchemy Homework - Surfs Up!

![surfs-up.png](Images/surfs-up.png)

## Step 1 - Climate Analysis and Exploration

Python and SQLAlchemy were used to do basic climate analysis and data exploration of the Hawaiian climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* The [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files were provided to complete the climate analysis and data exploration.

* SQLAlchemy `create_engine` was used to connect to the sqlite database.

* SQLAlchemy `automap_base()` was used to reflect tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Python was linked to the database by creating an SQLAlchemy session.

* **Important** Don't forget to close out your session at the end of your notebook.

### Precipitation Analysis

* I retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. **Note** you do not pass in the date as a variable to your query.

* The `date` and `prcp` values were selected.

* The query results into a Pandas DataFrame and set the index was set to the date column.

* DataFrame values was sorted by `date`.

* DataFrame `plot` method was used.

  ![precipitation](Images/date_vs_precipatation.png)

* Pandas was used to print the summary statistics for the precipitation data.

### Station Analysis

* A query was designed to calculate the total number of stations in the dataset, 

* a query was designed to find the most active stations (i.e. which stations have the most rows?).

  * The stations and observation counts were listed in descending order.

  * The station with the highest number of observations was found.

  * Using the most active station id, the lowest, highest, and average temperature was calculated.

* A query was designed to retrieve the last 12 months of temperature observation data (TOBS).

    ![station-histogram](Images/TempratureObservationsUSC00519281station.png)

* Close out your session.

- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* We used pandas to perform this portion.

### Temperature Analysis II

* You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use "Trip Avg Temp" as the title.

  * Use the average temperature as the bar height (y value).

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/TripAvgerageTemperature.png)

### Daily Rainfall Average

* Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!

* Calculate the rainfall per weather station using the previous year's matching dates.

  * Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

  * Set the start and end date of the trip.

  * Use the date to create a range of dates.

  * Strip off the year and save a list of strings in the format `%m-%d`.

  * Use the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/TemperaturesBetween8-1-2017-8-7-2017.png)

* Close out your session.

