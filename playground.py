from read_r import align_call_row
import re

# merge_headers('                                                                                   SETT. PRICE IMM INDEX              RTH       GLOBEX®            OPEN        ----CONTRACT----', 'OPEN RANGE          HIGH            LOW         CLOSING RANGE        DISCOUNT % PT.CHGE.##              VOLUME    VOLUME       INTEREST             HIGH      LOW')
# print(re.split('[  ]{2,}(?![^()]*\))', "d   ( h    2.95 )"))
# l = ['EURODOLLAR CALLS', 'SETT.PRICE                     EXER    RTH       GLOBEX            OPEN        --CONTRACT--', 'STRIKE OPEN RANGE                 HIGH          LOW        CLOSING RANGE       & PT.CHGE.           DELTA     CISES   VOLUME    VOLUME       INTEREST         HIGH     LOW']
# header = ',,STRIKE,OPEN RANGE, HIGH,LOW,CLOSING RANGE,SETT.PRICE & PT.CHGE.,EXER CISES,RTH VOLUME,GLOBEX VOLUME,OPEN INTEREST,CONTRACT  (HIGH  LOW)'
# row = 'OCT18,EURO DLR CALL,9737,----,----,----,0.002N,.005+,0.2,.194,----,2158,2158,136934 +,782 .190B,.010A'
#
# align_call_row(header, row)

x = '3 ----'

print(re.sub(r'(\d)( ----)', r'\1 \2', x))