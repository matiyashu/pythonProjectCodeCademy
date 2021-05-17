"""
###### TASK #####

Analyzing Ad Sources
1.
Examine the first few rows of ad_clicks.


Hint
Try pasting the following code:

print(ad_clicks.head())
2.
Your manager wants to know which ad platform is getting you the most views.

How many views (i.e., rows of the table) came from each utm_source?


Hint
Try using the following code:

ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()
3.
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.


Stuck? Get a hint
4.
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.


Stuck? Get a hint
5.
Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

Save your results to the variable clicks_pivot.


Stuck? Get a hint
6.
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?


Stuck? Get a hint
Analyzing an A/B Test
7.
The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both adds?


Stuck? Get a hint
8.
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.


Stuck? Get a hint
9.
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.


Stuck? Get a hint
10.
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.


Stuck? Get a hint
11.
Compare the results for A and B. What happened over the course of the week?

Do you recommend that your company use Ad A or Ad B?

Scrpit: >>>>>>>
"""

import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

utm_source_max = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print utm_source_max

#3 True and False column
ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()
  
print ad_clicks
	
#4
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print clicks_by_source

#5 PIVOT
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id')
print clicks_pivot
#6
clicks_pivot['percent_clicked'] = \
	clicks_pivot[True] /\
  (clicks_pivot[True] + 
  clicks_pivot[False])
  
print clicks_pivot

#7 experimental group
count = ad_clicks.groupby('experimental_group').user_id.count()
print count

#8
experimental = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

experimental_pivot = experimental.pivot(columns='is_click', index='experimental_group', values='user_id')
experimental_pivot['percent_clicked'] = \
	experimental_pivot[True] /\
  (experimental_pivot[True] + 
  experimental_pivot[False])
print experimental_pivot

#9
a_clicks= ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks= ad_clicks[ad_clicks.experimental_group == 'B']

#10
aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

aclicks_pivot = aclicks.pivot(columns='is_click',index='day',values='user_id')
aclicks_pivot['percent_clicked'] = \
	aclicks_pivot[True] /\
  (aclicks_pivot[True] + 
  aclicks_pivot[False])
print aclicks_pivot
bclicks_pivot = bclicks.pivot(columns='is_click',index='day',values='user_id')
bclicks_pivot['percent_clicked'] = \
	bclicks_pivot[True] /\
  (bclicks_pivot[True] + 
  bclicks_pivot[False])
print bclicks_pivot
