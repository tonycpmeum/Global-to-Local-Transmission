from pandas import Series, DataFrame, MultiIndex

def clean_api_response(data: Series | DataFrame, name: str) -> DataFrame:
   if isinstance(data, Series):
      data = data.to_frame(name=name)

   if data.empty:
      raise ValueError(f"{name} returned no data")

   if isinstance(data.columns, MultiIndex):
      data.columns = data.columns.droplevel(1)

   data.columns.name = None
   data.index.name = 'date'

   return data