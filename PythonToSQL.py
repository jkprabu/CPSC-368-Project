import pandas as pd
import numpy as np

WB_Data_df = pd.read_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/WBData.xlsx", sheet_name="Data")
WB_Country_df = pd.read_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/WBData.xlsx", sheet_name="Country")
ESG_Data_df = pd.read_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/ESGEXCEL.xlsx", sheet_name="Data")
CA_Data_df = pd.read_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/RawClimateAgreements.xlsx")

WB_Data_df.set_index('Country code', inplace=True)
WB_Country_df.set_index('Country code', inplace=True)
ESG_Data_df.set_index('Country Code', inplace=True)
CA_Data_df.set_index('Country', inplace=True)

WB_Data_df = WB_Data_df.replace('..', "NULL")
WB_Country_df = WB_Country_df.replace('..', "NULL")
ESG_Data_df = ESG_Data_df.replace('..', "NULL")
CA_Data_df = CA_Data_df.fillna('NULL')

# Climate data stuff

ClimateData_inserts = []

ProjectedAnnualTemperatureChange_df     = WB_Data_df[WB_Data_df['Series name'] == 'Projected annual temperature change (2045-2065, Celsius)'][2011]
ProjectedAnnualPrecipitationChange_df   = WB_Data_df[WB_Data_df['Series name'] == 'Projected annual precipitation change (2045-2065, mm)'][2011]
AverageDailyMinMaxTemperature_df        = WB_Data_df[WB_Data_df['Series name'] == 'Average daily min/max temperature (1961-1990, Celsius)'][2011]
RenewableEnergyTarget_df                = WB_Data_df[WB_Data_df['Series name'] == 'Renewable energy target'][2011]
DroughtsFloodsExtremeTemperatures_df    = WB_Data_df[WB_Data_df['Series name'] == 'Droughts, floods, extreme temps (% pop. avg. 1990-2009)'][2009]
EmissionsPerCapita_df                   = WB_Data_df[WB_Data_df['Series name'] == 'CO2 emissions per capita (metric tons)'][2008]
RenewableElectricityOutput_df           = ESG_Data_df[ESG_Data_df['Indicator Name'] == 'Renewable electricity output (% of total electricity output)']['2015']


for ctrCd in WB_Data_df.index:
    PATC = ProjectedAnnualTemperatureChange_df.get(ctrCd, "NULL")
    PAPC = ProjectedAnnualPrecipitationChange_df.get(ctrCd, "NULL")
    ADMT = AverageDailyMinMaxTemperature_df.get(ctrCd, "NULL")
    DFET = DroughtsFloodsExtremeTemperatures_df.get(ctrCd, "NULL")
    EPC  = EmissionsPerCapita_df.get(ctrCd, "NULL")
    RET  = RenewableEnergyTarget_df.get(ctrCd, "NULL")
    REO  = RenewableElectricityOutput_df.get(ctrCd, "NULL")

    attrs = "CountryCode, ProjectedAnnualTemperatureChange, ProjectedAnnualPrecipitationChange, AverageDailyMinMaxTemperature, DroughtsFloodsExtremeTemperatures, EmissionsPerCapita, RenewableEnergyTarget, RenewableElectricityOutput"
    values = f"\"{ctrCd}\", \"{PATC}\", \"{PAPC}\", \"{ADMT}\", {DFET}, {EPC}, \"{RET}\", {REO}"
    ClimateData_inserts.append(f"INSERT INTO ClimateData ({attrs}) VALUES ({values});")

ClimateData_inserts = [ins.replace("\"NULL\"", "NULL") for ins in ClimateData_inserts]

# Country stuff

Country_inserts = []

Name_df = WB_Country_df['Country name']
Population_df = WB_Data_df[WB_Data_df['Series name'] == 'Population'][2010]
PopulationGrowthPercent_df = WB_Data_df[WB_Data_df['Series name'] == 'Population growth (annual %)'][2010]
RegionName_df = WB_Country_df['Region']
CapitalCity_df = WB_Country_df['Capital city']
IncomeGroup_df = WB_Country_df['Income group']
GDP_df = WB_Data_df[WB_Data_df['Series name'] == 'GDP ($)'][2010]
UrbanPopulation_df = WB_Data_df[WB_Data_df['Series name'] == 'Urban population'][2010]
UrbanPopulationGrowth_df = WB_Data_df[WB_Data_df['Series name'] == 'Urban population growth (annual %)'][2010]
GovernmentEffectiveness_df = ESG_Data_df[ESG_Data_df['Indicator Name'] == 'Government Effectiveness: Estimate']['2022']
ControlOfCorruption_df = ESG_Data_df[ESG_Data_df['Indicator Name'] == 'Control of Corruption: Estimate']['2022']
DevelopedOrDeveloping_df = WB_Country_df['DevelopedOrDeveloping']


for ctrCd in WB_Data_df.index:
    NM = Name_df[ctrCd]
    P = Population_df.get(ctrCd, "NULL")
    PGP = PopulationGrowthPercent_df.get(ctrCd, "NULL")
    RN = RegionName_df.get(ctrCd, "NULL")
    CC = CapitalCity_df.get(ctrCd, "NULL")
    IG = IncomeGroup_df.get(ctrCd, "NULL")
    GDP = GDP_df.get(ctrCd, "NULL")
    UP = UrbanPopulation_df.get(ctrCd, "NULL")
    UPG = UrbanPopulationGrowth_df.get(ctrCd, "NULL")
    GE = GovernmentEffectiveness_df.get(ctrCd, "NULL")
    COC = ControlOfCorruption_df.get(ctrCd, "NULL")
    DOD = DevelopedOrDeveloping_df.get(ctrCd, "NULL")

    attrs = "Name, CountryCode, Population, PopulationGrowthPercent, RegionName, CapitalCity, IncomeGroup, GDP, UrbanPopulation, UrbanPopulationGrowth, GovernmentEffectiveness, ControlOfCorruption, DevelopedOrDeveloping"
    values = f"\"{NM}\", \"{ctrCd}\", {P}, {PGP}, \"{RN}\", \"{CC}\", \"{IG}\", {GDP}, {UP}, {UPG}, {GE}, {COC}, \"{DOD}\""
    Country_inserts.append(f"INSERT INTO Country ({attrs}) VALUES ({values});")

Country_inserts = [ins.replace("\"NULL\"", "NULL") for ins in Country_inserts]    

# ClimateAgreement stuff

ClimateAgreement_inserts = []

CountryName_df = CA_Data_df.index
AgreementName30_df = ['Paris']*len(CountryName_df)
DateSigned30_df = CA_Data_df['2030_Target_Last_Updated']
Target30_df = CA_Data_df['NDC_Target_Text']
TargetDate30_df = ['2030']*len(CountryName_df)

AgreementName50_df = ['Net Zero']*len(CountryName_df)
DateSigned50_df = CA_Data_df['2050_Target_Last_Updated']
Target50_df = CA_Data_df['Net_Zero_Target_Text']
TargetDate50_df = ['2050']*len(CountryName_df)

for ctrNm in CountryName_df:
    AGR30 = 'Paris'
    DS30 = DateSigned30_df.get(ctrNm, "NULL") 
    T30 = Target30_df.get(ctrNm, "NULL") 
    TD30 = '2030'

    AGR50 = 'Net Zero'
    DS50 = DateSigned50_df.get(ctrNm, "NULL") 
    T50 = Target50_df.get(ctrNm, "NULL") 
    TD50 = '2050'

    attrs = "CountryName, AgreementName, DateSigned, Target , TargetDate"
    val30 = f"\"{ctrNm}\", \"{AGR30}\", {DS30}, \"{T30}\", {TD30}"
    val50 = f"\"{ctrNm}\", \"{AGR50}\", {DS50}, \"{T50}\", {TD50}"
    ClimateAgreement_inserts.append(f"INSERT INTO Country ({attrs}) VALUES ({val30});")
    ClimateAgreement_inserts.append(f"INSERT INTO Country ({attrs}) VALUES ({val50});")

ClimateAgreement_inserts = [ins.replace("\"NULL\"", "NULL") for ins in ClimateAgreement_inserts]    

df = pd.DataFrame(ClimateData_inserts)
df.to_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/ClimateData_inserts.xlsx")

df = pd.DataFrame(Country_inserts)
df.to_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/Country_inserts.xlsx")

df = pd.DataFrame(ClimateAgreement_inserts)
df.to_excel("/Users/cpt.flippers/Documents/CS 368/Project/SQL DDL/ClimateAgreement_inserts.xlsx")