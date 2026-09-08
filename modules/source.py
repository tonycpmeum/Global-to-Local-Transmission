from dataclasses import dataclass
from typing import Optional, Tuple
from pandas import Timestamp

RAW_DATA_PATH = '../data/raw'
PROCESSED_DATA_PATH = '../data/processed'
OUTPUT_FOLDER_PATH = '../output'
parquet_monthly = f"{PROCESSED_DATA_PATH}/monthly.parquet"
parquet_daily = f"{PROCESSED_DATA_PATH}/daily.parquet"

fed_regimes: dict[list[tuple[Timestamp]]] = {
   "hiking": [
      (Timestamp('2015-12-17'), Timestamp('2019-07-30')), 
      (Timestamp('2022-03-17'), Timestamp('2024-09-17'))
      ],
   "cutting": [
      (Timestamp('2019-07-31'), Timestamp('2020-03-02')), 
      (Timestamp('2024-09-18'), Timestamp('2025-12-10'))
      ],
   'flat': [
      (Timestamp('2015-01-01'), Timestamp('2015-12-16')),
      (Timestamp('2025-12-11'), Timestamp('2026-08-25'))
      ],
   "covid_EXCLUDE": [(Timestamp('2020-03-03'), Timestamp('2022-03-16'))]
}

class Source(str):
   ticker: Optional[str]
   def __new__(cls, name: str, ticker: Optional[str] = None) -> "Source":
      obj = super().__new__(cls, name)
      obj.ticker = ticker
      return obj
    
@dataclass(frozen=True)
class Sources:
   OPR = Source('OPR')
   MGS_10Y = Source('MGS_10Y')
   FFR_midpoint = Source('FFR_midpoint')
   cpi_inflation_yoy = Source('cpi_inflation_yoy')
   UST_10Y = Source('UST_10Y', '^TNX')
   USDMYR = Source('USDMYR', 'MYR=X')
   DXY = Source('DXY', 'DX-Y.NYB')
   VIX = Source('VIX', '^VIX')
   brent_oil = Source('Brent_Oil', 'BZ=F')
   palm_oil_global = Source('Palm_Oil', 'PPOILUSDM')
   KLCI = Source('KLCI', '^KLSE')
   financials = Source('financials')
   plantation = Source('plantation')
   REITs = Source('REITs')
   technology = Source('technology')
   energy = Source('energy')
   industrial_products = Source('industrial_products')

   low_freq: Tuple[Source, ...] = (Source('OPR'), Source('cpi_inflation_yoy'), Source('Palm_Oil', 'PPOILUSDM'))
   us_market: Tuple[Source, ...] = (Source('EFFR', 'DFF'), Source('UST_10Y', '^TNX'), Source('DXY', 'DX-Y.NYB'), Source('VIX', '^VIX'), Source('Brent_Oil', 'BZ=F'))
   my_market: Tuple[Source, ...] = (
      Source('KLCI', '^KLSE'), Source('financials'), Source('plantation'), Source('REITs'), Source('technology'), Source('energy'), Source('industrial_products')
   )

