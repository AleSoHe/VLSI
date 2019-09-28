TEX = pdflatex --shell-escape
PGF = $(addsuffix .pdf, $(basename $(wildcard pgf/*.tex)))

.PHONY: view

view: main.pdf
	okular main.pdf
	
main.pdf: main.tex sections/*.tex figs
	$(TEX) main.tex

pgf/%.pdf: pgf/%.tex
	cd pgf; pdflatex ../$< 

figs: $(PGF)

clean: 
	rm *.aux *.log
	
