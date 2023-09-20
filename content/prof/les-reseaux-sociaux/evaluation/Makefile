# Ce Makefile ne construit ni les sujets, ni les corrigés. C'est volontaire.

ODT:=$(wildcard reseaux-sociaux-devoir?-blanc.odt)
PDF:=$(ODT:.odt=.pdf)

all: ${PDF}

%.pdf: %.odt
	libreoffice --headless --convert-to pdf $(<F)
