TEX = pdflatex --shell-escape
PGF = pgf/1a_N_step.tex pgf/2a_char_curve.tex

.PHONY: all view

view: main.pdf
	okular main.pdf
	
main.pdf: main.tex sections/*.tex $(PGF)
	$(TEX) main.tex
	
images: $(PGF)
	cd pgf; pdflatex ../$^
