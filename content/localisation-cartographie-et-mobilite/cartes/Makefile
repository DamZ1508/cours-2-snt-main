all: villes.png

%.pdf: %.tex
	spix $<

villes.png: villes.pdf
	convert -density 150 villes.pdf -quality 90 -resize 300 villes.png
