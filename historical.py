import ftplib
import os
import zipfile
import subprocess
import json

output_directory = r"C:\Users\npredey\Downloads\CMEHistoricalData"


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


def parse_historical_data(output_directory, pages=None):
    if pages is None:
        pages = [51]
    for filename in os.listdir(output_directory):
        unzipped_file = os.path.join(output_directory, filename.split('.')[0])
        full_filepath = os.path.join(output_directory, filename)
        if zipfile.is_zipfile(full_filepath) and not os.path.exists(unzipped_file):
            with zipfile.ZipFile(full_filepath, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(output_directory, unzipped_file))
        if os.path.exists(unzipped_file):
            print(unzipped_file)
            for pdf_filename in os.listdir(unzipped_file):
                pages_with_section = set(["Section{}".format(page) for page in pages])
                bulletin_section = pdf_filename.split('_')[0]
                if bulletin_section in pages_with_section:
                    section_filename = os.path.join(output_directory, unzipped_file, pdf_filename)
                    output = subprocess.check_output("\"C:\\Users\\npredey\\Downloads\\R\\R-3.5.1\\bin\\Rscript.exe\" ReadPDF.R {}".format(section_filename))
                    output = output.decode('utf-8')
                    for line in output:
                        print("DD", line)
                    # data = json.loads(output.decode('utf-8'))
                    # print(data)


# get_historical_data(output_directory)
parse_historical_data(output_directory)
