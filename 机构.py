from sqlalchemy import create_engine
import tushare as ts
#engine = create_engine('mysql+pymysql://root:toor@127.0.0.1/packageing?charset=utf8')
engine = create_engine('mysql+pymysql://root:toor@127.0.0.1/gupiao?charset=utf8')

df = ts.inst_detail()
de = ts.inst_tops()
broker = ts.broker_tops()

#df.to_sql('inst_datail',engine)
#de.to_sql('inst_tops',engine)
#broker.to_sql('broker_tops',engine)

df.to_sql('inst_datail',engine,if_exists='append')
de.to_sql('inst_tops',engine,if_exists='append')
#broker.to_sql('broker_tops',engine,if_exists='append')
