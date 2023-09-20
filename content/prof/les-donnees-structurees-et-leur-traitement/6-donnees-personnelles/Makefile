all: corpus.pdf corpus.tar.xz

corpus.pdf: corpus.tex corpus/*tex
	spix corpus.tex
	PDFBACKEND=pypdf2 pdfautonup -o corpus.pdf corpus.pdf

corpus.tar.xz:
	tar -cvJf corpus.tar.xz corpus.tex corpus/*tex
