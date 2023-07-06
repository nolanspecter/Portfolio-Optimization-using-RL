TICKERS = ['JNJ', 'KO', 'T']
FILEPATH = 'preprocessed.csv'
EPISODE_LENGTH = 252*5*3 #5 years. Multiply 3 for indexing each stocks
OBS_COL = ['JNJ_rsi',
 'KO_rsi',
 'T_rsi',
 'JNJ_macd',
 'KO_macd',
 'T_macd',
 'JNJ_obv',
 'KO_obv',
 'T_obv',
 'JNJ_h/o',
 'KO_h/o',
 'T_h/o',
 'JNJ_l/o',
 'KO_l/o',
 'T_l/o',
 'JNJ_c/o',
 'KO_c/o',
 'T_c/o',
 'JNJ_open_change',
 'KO_open_change',
 'T_open_change',
 'JNJ_close_change',
 'KO_close_change',
 'T_close_change',
 'JNJ_volume_change',
 'KO_volume_change',
 'T_volume_change',
 'JNJ_open_change_change_mean_7',
 'KO_open_change_change_mean_7',
 'T_open_change_change_mean_7',
 'JNJ_open_change_change_mean_14',
 'KO_open_change_change_mean_14',
 'T_open_change_change_mean_14',
 'JNJ_open_change_change_mean_30',
 'KO_open_change_change_mean_30',
 'T_open_change_change_mean_30',
 'JNJ_close_change_change_mean_7',
 'KO_close_change_change_mean_7',
 'T_close_change_change_mean_7',
 'JNJ_close_change_change_mean_14',
 'KO_close_change_change_mean_14',
 'T_close_change_change_mean_14',
 'JNJ_close_change_change_mean_30',
 'KO_close_change_change_mean_30',
 'T_close_change_change_mean_30',
 'JNJ_volume_change_change_mean_7',
 'KO_volume_change_change_mean_7',
 'T_volume_change_change_mean_7',
 'JNJ_volume_change_change_mean_14',
 'KO_volume_change_change_mean_14',
 'T_volume_change_change_mean_14',
 'JNJ_volume_change_change_mean_30',
 'KO_volume_change_change_mean_30',
 'T_volume_change_change_mean_30',
 'JNJ_h/o_change_mean_7',
 'KO_h/o_change_mean_7',
 'T_h/o_change_mean_7',
 'JNJ_h/o_change_mean_14',
 'KO_h/o_change_mean_14',
 'T_h/o_change_mean_14',
 'JNJ_h/o_change_mean_30',
 'KO_h/o_change_mean_30',
 'T_h/o_change_mean_30',
 'JNJ_l/o_change_mean_7',
 'KO_l/o_change_mean_7',
 'T_l/o_change_mean_7',
 'JNJ_l/o_change_mean_14',
 'KO_l/o_change_mean_14',
 'T_l/o_change_mean_14',
 'JNJ_l/o_change_mean_30',
 'KO_l/o_change_mean_30',
 'T_l/o_change_mean_30',
 'JNJ_c/o_change_mean_7',
 'KO_c/o_change_mean_7',
 'T_c/o_change_mean_7',
 'JNJ_c/o_change_mean_14',
 'KO_c/o_change_mean_14',
 'T_c/o_change_mean_14',
 'JNJ_c/o_change_mean_30',
 'KO_c/o_change_mean_30',
 'T_c/o_change_mean_30']

EN_COLS = ['rsi', 'macd', 'obv', 'h/o', 'l/o', 'c/o', 'open_change',
       'close_change', 'volume_change', 'open_change_change_mean_7',
       'open_change_change_mean_14', 'open_change_change_mean_30',
       'close_change_change_mean_7', 'close_change_change_mean_14',
       'close_change_change_mean_30', 'volume_change_change_mean_7',
       'volume_change_change_mean_14', 'volume_change_change_mean_30',
       'h/o_change_mean_7', 'h/o_change_mean_14', 'h/o_change_mean_30',
       'l/o_change_mean_7', 'l/o_change_mean_14', 'l/o_change_mean_30',
       'c/o_change_mean_7', 'c/o_change_mean_14', 'c/o_change_mean_30']

COLS = ['High', 'Low', 'Open', 'Close', 'Volume']