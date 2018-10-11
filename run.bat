SET z='temp.txt'
echo.%z%

"C:\Users\npredey\Downloads\R\R-3.5.1\bin\Rscript.exe" ReadPDF.R "C:\Users\npredey\Downloads\Section51_Euro_Dollar_Call_Options_(1).pdf"
"C:\Users\npredey\Downloads\R\R-3.5.1\bin\Rscript.exe" -e "args<-commandArgs(TRUE);date <- trimws(toString(Sys.Date()));filename <- tools::file_path_sans_ext(basename(args[1]));ext <- '.txt';f <- paste(filename, date, ext, sep='');cat(f);" "C:\Users\npredey\Downloads\Section51_Euro_Dollar_Call_Options_(1).pdf" > z

set /p filename= < z
del z
echo.%filename%

py main.py %filename%
pause