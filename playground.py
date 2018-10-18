from read_oi import align_call_row
import re
import ondemand

od = ondemand.OnDemandClient(api_key='24f1ed790cd88e42a2ca252e8beb15b6', end_point='https://marketdata.websol.barchart.com/')

quotes = od.quote_eod(symbols='GE', exchange='CME')
print(quotes)
