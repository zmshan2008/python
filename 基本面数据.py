from sqlalchemy import create_engine
import tushare as ts
engine = create_engine('mysql+pymysql://root:toor@localhost/gupiao?charset=utf8')

stock = ts.get_stock_basics()
#stock.to_sql('stock_basics',engine)
stock.to_sql('stock_basics',engine,if_exists='append')
#print(stock)

profit = ts.get_profit_data(2015,3)
#profit.to_sql('profit_data',engine)
profit.to_sql('profit_data',engine,if_exists='append')

operation = ts.get_operation_data(2015,3)
#operation.to_sql('operation_data',engine)
operation.to_sql('operation_data',engine,if_exists='append')

growth = ts.get_growth_data(2015,3)
#growth.to_sql('growth_data',engine)
growth.to_sql('growth_data',engine,if_exists='append')

debtpaying = ts.get_debtpaying_data(2015,3)
#debtpaying.to_sql('debtpaying_data',engine)
debtpaying.to_sql('debtpaying_data',engine,if_exists='append')

cashflow = ts.get_cashflow_data(2015,3)
#cashflow.to_sql('cashflow_data',engine)
cashflow.to_sql('cashflow_data',engine,if_exists='append')

