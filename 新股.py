import tushare as ts
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:zmshan421182@192.168.1.10/packageing?charset=utf8')

df = ts.new_stocks()
#df.to_sql('new_stocks',engine)
df.to_sql('new_stocks',engine,if_exists='append')

holdings = ts.fund_holdings(2015,1)
#holdings.to_sql('fund_holdings',engine)
holdings.to_sql('fund_holdings',engine,if_exists='append')

