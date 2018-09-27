import ftplib
import os


def get_historical_data(output_directory=''):
    cme_ftp = ftplib.FTP('ftp.cmegroup.com')
    cme_ftp.login()
    cme_ftp.cwd('/bulletin')
    files = cme_ftp.nlst()

    for f in files:
        print("Writing data to: {}".format(f))
        output_cme_file = os.path.join(output_directory, f)
        if os.path.exists(output_cme_file):
            print("file exists. skipping this file..")
            continue
        cme_zip_file = open(output_cme_file, 'wb')
        cme_ftp.retrbinary('RETR {}'.format(f), cme_zip_file.write)
        cme_zip_file.close()


