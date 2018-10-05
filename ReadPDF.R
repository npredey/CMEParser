#!/usr/bin/R

library(pdftools)
args = commandArgs(trailingOnly=TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
  print(args[1])
}
text_file <- args[1]
txt <- pdf_text(text_file)
fileConn<-file("output.txt")
writeLines(txt, fileConn)
close(fileConn)