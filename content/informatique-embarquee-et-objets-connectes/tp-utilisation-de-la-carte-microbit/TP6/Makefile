all: automate.png bilan.pdf

%.png: %.pdf
	pdftoppm -png -singlefile $< $$(basename $@ .png)

%.pdf: %.tex
	spix $<
