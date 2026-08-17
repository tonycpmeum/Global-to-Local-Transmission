from dataclasses import dataclass
from typing import Optional, Tuple

class Source(str):
   ticker: Optional[str]

   def __new__(cls, name: str, ticker: Optional[str] = None) -> "Source":
      obj = super().__new__(cls, name)
      obj.ticker = ticker
      return obj
    
@dataclass(frozen=True)
class Sources:
   OPR = Source('OPR')
   cpi_inflation_yoy = Source('cpi_inflation_yoy')
   EFFR = Source('EFFR', 'DFF')
   UST_10Y = Source('UST_10Y', '^TNX')
   USDMYR = Source('USDMYR', 'MYR=X')
   DXY = Source('DXY', 'DX-Y.NYB')
   VIX = Source('VIX', '^VIX')
   brent_oil = Source('Brent_Oil', 'BZ=F')
   palm_oil_global = Source('Palm_Oil', 'PPOILUSDM')
   KLCI = Source('KLCI', '^KLSE')
   financials = Source('financials')
   plantation = Source('plantation')
   reits = Source('reits')
   technology = Source('technology')
   energy = Source('energy')
   industrial_products = Source('industrial_products')

   low_freq: Tuple[Source, ...] = (Source('OPR'), Source('cpi_inflation_yoy'), Source('Palm_Oil', 'PPOILUSDM'))
   us_market: Tuple[Source, ...] = (Source('EFFR', 'DFF'), Source('UST_10Y', '^TNX'), Source('DXY', 'DX-Y.NYB'), Source('VIX', '^VIX'), Source('Brent_Oil', 'BZ=F'))
   my_market: Tuple[Source, ...] = (
      Source('KLCI', '^KLSE'), Source('financials'), Source('plantation'), Source('reits'), Source('technology'), Source('energy'), Source('industrial_products')
   )

RAW_DATA_PATH = '../data/raw'
PROCESSED_DATA_PATH = ''