# CPSC-368-Project

## Summary of data analysis:
1. Do Countries Follow Through on Climate Agreements?
Countries occasionally band together and sign climate accords agreeing to reduce their greenhouse gas emissions. However, some countries may choose to deviate from their intended reduction target because it is costly to transition away from greenhouse gas emitting production. In this analysis, we investigate how countries follow through on their commitments to international climate agreements: specifically, we look at countries that signed the Paris Climate Accord in 2016. We focus on the correlational analysis of countries. From our analysis, we find answers to our research questions.
2. Do countries follow through on their climate agreements? We find that the answer to this depends on the country. Figure 3 shows which countries were the most/least effective at reducing their CO2 emissions from 2016 to 2020 (post-treaty).
3. Is government effectiveness for treaty-signing countries related to a reduction in CO2 emissions? Yes. We see in Figure 4 that countries with high government effectiveness also had proportional reductions in their CO2 emissions.
Were treaty-signing countries any more effective than non-treaty-signing countries at reducing CO2 emissions? No. We find from regression specifications 1 and 2 that treaty-singing countries reduced their CO2 emissions by as much as non-treaty signing countries in the 4 years post-treaty.
4. Are there differences in post-treaty commitment to CO2 emission reduction between developed and developing countries? Yes. From Fig. 5 & 6 and regression specifications 3 and 4, we find that developed countries and significantly more effective at decreasing their CO2 emissions than developing countries.

Overall, while climate agreements are important in unifying efforts to reach specific climate metrics like reduction in CO2 emissions, it is important to consider factors like government effectiveness and heterogeneity in country characteristics such as development when evaluating country follow-through on climate agreements. In particular, we find that looking at the performance of non-treaty-signing countries is highly informative in evaluating the performance of treaty-signing countries.

## Steps for replication:
1. Connect to personal ORACLE server
2. Run all.sql 
3. Install all dependencies mentioned below
3. Run final_climate_analysis.ipynb
4. Witness the marvel :)


### Run these commands:
- pip install pandas
- pip install numpy
- pip install altair
- pip install matplotlib
- pip install statsmodels
- pip install pysal 
- pip install oracledb