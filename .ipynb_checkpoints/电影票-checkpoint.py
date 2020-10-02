import tushare as ts
from sqlalchemy import create_engine
token = ts.set_token('c723069dd4a25402d05ea6afad36da2937111adf012f8258abb5f7e05936e575')
#engine = create_engine('mysql+pymysql://root:wuwo421182@192.168.1.9/packageing?charset=utf8')
engine = create_engine('mysql+pymysql://root:toor@127.0.0.1/test?charset=utf8')

realtime = ts.realtime_boxoffice()
#realtime.to_sql('realtime_boxoffice',engine)
realtime.to_sql('realtime_boxoffice',engine,if_exists='append')

day = ts.day_boxoffice()
#day.to_sql('day_boxoffice',engine)
day.to_sql('day_boxoffice',engine,if_exists='append')

month = ts.month_boxoffice()
#month.to_sql('month_boxoffice',engine)
month.to_sql('month_boxoffice',engine,if_exists='append')

cinema = ts.day_cinema()
#cinema.to_sql('day_cinema',engine)
cinema.to_sql('day_cinema',engine,if_exists='append')

