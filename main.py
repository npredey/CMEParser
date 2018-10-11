from historical import get_historical_data
from read_oi import read
import sys

# get_historical_data(output_directory="/Users/nickpredey/EDF_MAN/data/CME/")
# get_historical_data(output_directory=r'C:\Users\npredey\Downloads\CME')


def main():
    filepath = ''
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Filepath must be specified")
        exit()
    print(filepath)
    read(filepath)


main()
