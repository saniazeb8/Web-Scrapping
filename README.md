# Data Collection Exercise for Sentiment Analysis
# Tiger Parenting

### Summary
This study investigates the evolution of parental care in contemporary societies, marked by increased involvement and prolonged investment in child-rearing, to understand its effects on family dynamics and societal health. It aims to analyze trends in parental time investment from 2003 to 2022 in the U.S., focusing on gender differences, educational gradient of parents, variations in childcare activities, and age group disparities. Additionally, it assesses the impact of parent's income on parental time investment, leveraging U.S. Census data and state-level heatmaps. The research also explores the experiences of parents practicing intensive parenting, examining the trade-offs between child-rearing and other life facets and their emotions when engaging in childcare-related discussions. Through this analysis, the study seeks to provide insights into the current dynamics of parental care and their wider societal implications, especially concerning intergenerational equity and well-being.

### Project Goals
* Our project seeks to build upon existing literature on parenting by examining the dynamics of parental time investment in child-rearing within modern societies.
* We aim to provide a comprehensive analysis of how parental involvement has evolved and the implications of these changes for parents. We provided a nuanced understanding of the contemporary patterns of parental care and the broader social and economic factors that shape them. Our goal is to contribute to the discourse on the evolving nature of family dynamics and the consequences of these changes for intergenerational equity and well-being.


### Research Questions  
* What are the Trends in Parental Time Investment with children from 2003 to 2022 in the U.S. population?  
    * Our investigation will delve into:
      * The overall trend of time investment between 2003 and 2022
      * Gender disparities in time investment with children. 
      * Variations in time allocation among different childcare activities.
      * Differences in time spent with children across various age groups

* How Does Socioeconomic Status Influence Parental Time Investment in Children?
   * Our investigation will delve into:
      * Parent's education level
      * Income level(using the state median income as proxy)    

* What Is the Parental Experience of Child-Rearing in the Context of Intensive Parenting?
  * Our investigation will delve into:
      * Parent's time use across different activities
      * Parent's experience on childcare or related topics      

### Overall Findings
* Parental time investment in their children continues to increase within recent decades
* Parents with higher socioeconomic status generally invest more in their children
* Intensive parenting practices are anticipated to be associated with a shift in parent’s time allocation
   * This reallocation of time is expected to be accompanied by negative psychological consequences for parents
* Parents generally experience negative emotions on topics related to childcare

### Data Sources
* **Data Source 1 - American Time Use Survey (ATUS)**  
Url: https://www.bls.gov/tus/data.htm  
Url: https://www.bls.gov/tus/data/datafiles-0322.htm (**the oversized data file**)  
The data consists of the responses of respondents from the year 2003 to 2022. The data contains demographic information of the respondents along with time spent on different diary activities on a 24-hour basis.

* **Data Source 2 - US Census Data - American Community Survey(API)**  
Url: https://data.census.gov/  
Url: https://api.census.gov/data/2022/acs/acs5/variables.html  
The ACS data contains socioeconomic and demographic data from respondents across the states.  

* **Data Source 3 - Parenting Forum - What to Expect(Scarpped)**  
Url: https://community.whattoexpect.com/forums/  
A parental forum where we scrapped comments from a dedicated parenting thread, where parents of 1-year-olds exchange insights, emotions, and inquiries concerning their child-rearing experiences.

* **Data Source 4 - Reddit - r/Parenting(API)**  
Url: https://www.reddit.com/r/Parenting/  
The subreddit contains comments from parents for different age groups of children.

### Github Navigation Steps  
* First clone the repository at your local machine.
* The structure of the repository is as follows:
   * Data folder contains all the CSV files
   * Notebooks folder contains all the iPython files of the codes
      * Census_ACS.ipynb file extracts the medium income level of U.S. states    
      * ATUS.ipynb file contains the preprocessing, exploratory data analysis, visualization, and OLS model results on the ATUS-related data file.  
      * The sentiment_analysis.ipynb file contains the preprocessing, emotion classification, and visualization through wordclods for the r/Parenting subreddit.  
      * The redditScrapper2.py and parental_forum_scrapper.py files contain the script for scrapping comments.
      * AI Assistance Use.text contains information regarding the use of AI assistance
      * Script folder contains Python script files for scrapping
* Presentation folder contains in-class and modified presentation slides and our extended version of project report


### Required Libraries  
1. python == 3.11.8
2. numpy == 1.26.1
3. pandas == 2.1.1
4. matplotlib = 3.8.2
5. seaborn == 0.13.1
6. statsmodels == 0.14.1
7. transformers == 4.38.2
8. praw == 7.7.1
9. openpyxl == 3.0.10
10. requests == 2.31.0
11. bs4 == 4.12.2
12. geopandas == 0.11.1
13. plotly == 5.9.0
14. scipy == 1.9.0
15. scikit-learn (sklearn) == 1.1.1


