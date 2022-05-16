def prepared_data(inspection_vi_df) :
    inspection_vi_df['YEAR'] = inspection_vi_df['ACTIVITY DATE'].str.split('/').str[2]
    inspection_vi_df['SEATS'] = inspection_vi_df['PE DESCRIPTION'].str.extract('(\(.*\))')
    inspection_vi_df = inspection_vi_df.dropna()
    return inspection_vi_df
