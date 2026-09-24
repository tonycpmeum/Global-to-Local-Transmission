from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple

RAW_DATA_PATH = '../data/raw'
PROCESSED_DATA_PATH = '../data/processed'
OUTPUT_FOLDER_PATH = '../output'
parquet_monthly = f"{PROCESSED_DATA_PATH}/monthly.parquet"
parquet_daily = f"{PROCESSED_DATA_PATH}/daily.parquet"
parquet_fomc =f"{PROCESSED_DATA_PATH}/fomc_event_data.parquet"

START = datetime(2015, 1, 1)
END = datetime(2026, 8, 25)

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
