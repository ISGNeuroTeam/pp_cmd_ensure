import pandas as pd
import numpy as np
from otlang.sdk.syntax import Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class EnsureCommand(BaseCommand):
    syntax = Syntax([Positional("columns", otl_type=OTLType.TEXT, inf=True)])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in self.get_iter("columns"):
            if col.value not in df.columns:
                df[col.value] = np.nan
        return df
