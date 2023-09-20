TEX:=$(wildcard *.tex)
PNG:=$(TEX:.tex=.png)

all: $(PNG)

%.png: %.pdf
	pdftoppm -png -singlefile $< $$(basename $@ .png)

%.pdf: %.tex
	spix $<
