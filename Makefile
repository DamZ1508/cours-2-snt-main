TEX := $(shell find content \( -type d -exec test -e "{}/Makefile" \; \) -prune -o -type f -regex ".*\.tex" -print)
ODT := $(shell find content \( -type d -exec test -e "{}/Makefile" \; \) -prune -o -type f -regex ".*\.odt" -print)
ODS := $(shell find content \( -type d -exec test -e "{}/Makefile" \; \) -prune -o -type f -regex ".*\.ods" -print)
ODP := $(shell find content \( -type d -exec test -e "{}/Makefile" \; \) -prune -o -type f -regex ".*\.odp" -print)
PDF := $(TEX:.tex=.pdf) $(ODT:.odt=.pdf) $(ODP:.odp=.pdf) $(ODS:.ods=.pdf)

DOT := $(shell find content \( -type d -exec test -e "{}/Makefile" \; \) -prune -o -type f -regex ".*\.dot" -print)
SVG := $(DOT:.dot=.svg)

# Où aller chercher les paquets LaTeX
export TEXINPUTS:=$(TEXINPUTS):$(PWD)/other/latex/

.PHONY: recursive build serve quick

all: build

.ONESHELL:
%.pdf: %.tex
	spix $<

.ONESHELL:
%.pdf: %.od?
	cd $(*D)
	libreoffice --headless --convert-to pdf $(<F)
	PDFBACKEND=pypdf2 pdfautonup $(@F) -o $(@F) || true

.ONESHELL:
%.svg: %.dot
	dot -Tsvg $< > $@

.ONESHELL:
recursive: FORCE
	find content -name Makefile -execdir make \;

build: recursive $(PDF) $(SVG)
	lektor build --output-path public

serve: recursive $(PDF) $(SVG)
	lektor serve

.ONESHELL:
loop:
	# J'obtiens souvent des segmentation fault…
	while true
	do
		make serve
	done

quick:
	lektor build

FORCE:
