#!/bin/bash
rm *.eps *.dvi *.log *.md5 *.ps; pdflatex -shell-escape -synctex=1 -interaction=nonstopmode drawing.tex 