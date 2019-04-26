# CMEParser
CMEParser does 2 things:

* Gets historical data from the CME site and puts it into a zip file.
* Parses that data (in pdf form) so that it is easier to read.

To run a sample, just run `main.py` to see an output to `strikes.csv`.
You can view `strikes.csv` in Excel, Notepad, or any other text editor.

Currently this project is on hold because the PDFs that the CME releases are all different, so one would need a new parser for each PDF.
