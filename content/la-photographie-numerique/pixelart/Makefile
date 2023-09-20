all: matrice-vierge.png matrice-rgb-france.png

%.pdf: %.tex
	spix $<

matrice-vierge.png: matrice-vierge.pdf
	convert -density 150 matrice-vierge.pdf -quality 90 -resize 500 matrice-vierge.png

matrice-rgb-france.png: matrice-rgb-france.pdf
	convert -density 150 matrice-rgb-france.pdf -quality 90 -resize 200 matrice-rgb-france.png
