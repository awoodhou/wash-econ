#Washington Economic Statistic Graphing


**To Run:**

* cd to the directory in Terminal
* $ python3 manage.py run server
* In a browser, go to ‘localhost:8000/regionaldata
* IT LIVES!! (or at least most of it does i think), check it out

The excel spreadsheet outlines the data that I have access to from BEA… The site is pulling from the categories in the ‘BEA RegionalData’ tab right now, the other two tabs have way more detailed data but aren’t in as generalized form, so I am setting those aside for now.

**To Do:**
* Include more data
* Let user change graphs dynamically (look & feel, presentation, change parameters, maybe include some sort of alternate table view, some way to compare similar graphs, etc.)
* Some way of indexing the different categories so the user can easily find what they are looking for (ideas: search, categories/tags)
* Make everything really pretty
* Maybe implement a categories database for easier category indexing, lets the site ‘know’ if the data being pulled from BEA has changed, categories have been added, etc.
* Any other features that we can think of that would improve user experience and usability

