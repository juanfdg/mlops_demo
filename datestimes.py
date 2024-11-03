def data_filtro(**context):
    print(context["logical_date"])



def prepare_data_train(**context):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler, LabelEncoder

    df = data_filtro(pd.Timestamp(context["logical_date"]))
    print("Data extracted!")