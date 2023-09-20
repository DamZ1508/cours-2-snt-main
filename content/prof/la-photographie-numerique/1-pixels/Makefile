all: evaluation1.pdf

evaluation1.pdf: evaluation1-a.pdf evaluation1-b.pdf
	PDFBACKEND=pypdf2 pdfautonup --output $@ $^

%.pdf: %.tex
	lualatex $<
