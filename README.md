# CMEParser
CMEParser is a respository for parsing [CME Daily Bulletin](https://www.cmegroup.com/market-data/daily-bulletin.html) publications, specifically those on interest rate products.

It seems that PDF parsing, at least in this case, seems to be easier/more fruitful in R. I am not entirely sure why. So, there is an R script that parses the PDF and puts it into a text file. This text file is read into a Python script and exported to a `csv` file.

Currently this project is on hold because the PDFs that the CME releases are all different, so one would need a new parser for each PDF.

To run a sample, just run `main.py` to see an output to `strikes.csv`.
You can view `strikes.csv` in Excel, Notepad, or any other text editor.

