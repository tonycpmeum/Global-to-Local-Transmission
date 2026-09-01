from pandas import Series, DataFrame, MultiIndex, to_numeric

def clean_api_response(data: Series | DataFrame, name: str) -> DataFrame:
   """Normalize Series/DataFrames from APIs into single header DataFrane."""
   if isinstance(data, Series):
      data = data.to_frame(name=name)

   if data.empty:
      raise ValueError(f"{name} returned no data")

   if isinstance(data.columns, MultiIndex):
      data.columns = data.columns.droplevel(1)

   data.columns.name = None
   data.index.name = 'date'
   return data

def parse_10y_entry(payload, date_str):
   """Extract the 10Y MGS entry from one day's response, or None if absent
   (public holiday, or a date BNM hasn't published for)."""
   mgs = payload.get("data", {}).get("malaysian_government_securities", [])
   ten_y = next((r for r in mgs if r.get("tenure", "").strip() == "10Y"), None)
   if ten_y is None:
      return None
   return {
      "date": date_str,
      "yield_close": to_numeric(ten_y.get("tra_yie_close")),
      "daily_change": to_numeric(ten_y.get("daily_change")),
      "tot_vol": to_numeric(ten_y.get("tot_vol")),
      "maturity_month": ten_y.get("maturity_month"),
      "maturity_year": ten_y.get("maturity_year"),
   }