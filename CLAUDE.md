# Mapping supply chain per industry

In this project we are developing a tracking and analysis system that allows us to map the supply chain relationship between companies.

## Data model

Each company is represented as a JSON object with following properties:

  - id (a unique identifier assigned upon insertion)
  - companyName (the company name in English)
  - industryCode : short name of the industry in English (E.g. Semiconductors)
  - ticker (if the given company is listed, carries the stock symbol)
  - description (the key product and focus)
  - marketCapInYen (market cap in JPY for this company)
  - PER
  - PBR
  - ESP
  - website : the URL to website
  - percentOfForeignOwnership
  - percentOfCirculatingEquity
  - latestPriceYen : the latest known stock price in JPY (if available)
  - ifForexSensitive : whether the company depends a lot on USD/JPY pair
  - a JSON array suppliers as company ids
  - a JSON array of client companies as company ids

## Company database

A collection of JSON records for multiple companies.

## Supplier chain graph

A view built from the available JSON files for companies showing who the supply chain.
 
## Data source

The agentic assistant will do online research and bring the data formatting it according to the specified JSON format,
building and expanding the database node by node iteratively.


## Methodology

The list of seed companies is as follows (Japanese companies):

  - Tokyo Seimitsu
  - Disco
  - Screen
  - Tokyo Electron
  - Advantest
  - Lasertech
  - Fujimi
  - 4004.T (this is a stock code, not a name)
  - 6890.T (this is a ticker symbol)
  - 4970.T
  - 6525.T (Kokusai)
  - 6856.T
  - 4368.T
  - 285A (this is a ticker symbol)
  - Hoya (7741.T)
  - Olympus (7733.T)