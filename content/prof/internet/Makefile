TEX:=$(wildcard *.tex)
PDF:=$(TEX:.tex=.pdf)

all: internet.pdf

internet.pdf: $(PDF)
	pdfautonup --size A5 tcp-ip.pdf debit.pdf --output - | pdfautonup topologie.pdf routage.pdf - cables.pdf neutralite.pdf --output internet.pdf

%.pdf: %.tex
	spix $<
