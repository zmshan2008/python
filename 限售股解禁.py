import tushare as ts
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:zmshan421182@192.168.1.10/packageing?charset=utf8')

df = ts.xsg_data()
#df.to_sql('xsg_data',engine)
df.to_sql('xsg_data',engine,if_exists='append')