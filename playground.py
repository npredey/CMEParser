import ftplib


def get_historical_data():
    f = ftplib.FTP('ftp.cmegroup.com')
    f.login()
    f.cwd('/bulletin')
    files = f.nlst()

    for fil in files:
        print(fil)
        some_file = open(fil, 'wb')
        response = f.retrbinary('RETR {}'.format(fil), some_file.write)
        some_file.close()


