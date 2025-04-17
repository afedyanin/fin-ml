import pandas as pd


class TimeSeriesComposer:
    def __init__(self):
        pass

    @staticmethod
    def shift_column(df: pd.DataFrame,
                     col_name: str,
                     count: int = 1,
                     shifted_col_suffix: str = '_T-') -> pd.DataFrame:
        for i in range(count):
            shifted_name = col_name + shifted_col_suffix + str(i+1)
            df[shifted_name] = df[col_name].shift(i+1)
        return df

