#!/usr/bin/R

library(pdftools)
args = commandArgs(trailingOnly=TRUE)
print(Sys.Date())
if (length(args)==0) {
  stop("At least one argument must be supplied (input file)", call.=FALSE)
} else if (length(args)==1) {
  print(args[1])
}
args[2] <- 100
text_file <- args[1]
txt <- pdf_text(text_file)
date <- trimws(toString(Sys.Date()))
filename <- tools::file_path_sans_ext(basename(text_file))
fileConn<-file(paste(filename, date, ".txt", sep=''))
writeLines(txt, fileConn)
close(fileConn)

date <- trimws(toString(Sys.Date()));filename <- tools::file_path_sans_ext(basename(args[1]));fileConn<-file(paste(filename, date, ".txt", sep=''));