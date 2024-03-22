CREATE TABLE Country (
    CountryCode CHAR(4),
    CountryName CHAR(50),
    Region CHAR(50),
    CapitalCity CHAR(50),
    IncomeGroup CHAR(50),
    GovernmentEffectiveness DECIMAL(6,3),
    PopulationDensity DECIMAL(8,3),
    DevelopedOrDeveloping CHAR(50),
    TradeBloc CHAR(50),
    PRIMARY KEY (CountryCode)
);

CREATE TABLE ClimateData(
    CountryCode CHAR(4),
    Year INTEGER,
    RenewableEnergyTarget CHAR(3), 
    RenewableEnergyOutput DECIMAL(5,2),
    RenewableEnergyConsumption DECIMAL(5,2),
    CO2 DECIMAL(7,4),
    Gini DECIMAL(5,2),
    TreeCoverLoss INTEGER,
    PRIMARY KEY (CountryCode, Year),
    FOREIGN KEY (CountryCode) REFERENCES Country
        ON DELETE CASCADE
); 

CREATE TABLE ClimateAgreement(
    CountryCode CHAR(4),
    CountryName CHAR(50),
    AgreementName CHAR(50), 
    DateSigned DATE, 
    Target CHAR(200), 
    TargetYear INTEGER, 
    PRIMARY KEY (CountryName, AgreementName),
    FOREIGN KEY (CountryCode) REFERENCES Country
        ON DELETE CASCADE
);

