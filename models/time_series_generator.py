import numpy as np
import pandas as pd
from datetime import datetime
from typing import Callable


class TimeSeriesGenerator:
    def __init__(self,
                 from_utc: datetime,
                 to_utc: datetime,
                 freq: str,
                 arg_step: float = 1):
        self._from = from_utc
        self._to = to_utc
        self._freq = freq
        self._arg_step = arg_step

    def generate(self,
                 func: Callable[[np.ndarray], np.ndarray],
                 col_name: str = "synthetic") -> pd.DataFrame:
        dates = pd.date_range(self._from, self._to, freq=self._freq)
        df_len = len(dates)
        step = self._arg_step
        stop = df_len * step
        arg = np.arange(start=0, stop=stop, step=step)
        price = func(arg)
        df = pd.DataFrame(pd.Series(price, dates, name=col_name))
        return df
