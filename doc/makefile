MAIN= paper
TEXPARTS= 	$(MAIN).tex 			

BIBPARTS= BIB/*.bib
FIGPARTS= FIG/*.pdf FIG/*.png
STYPARTS= mdwlist.sty
ALL= makefile  $(TEXPARTS) $(BIBPARTS) $(FIGPARTS) $(STYPARTS) README 

$(MAIN).pdf: $(MAIN).tex
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex

clean:
	\rm -f *.dvi *.bbl *.aux *.log *.blg *.toc

spotless: clean
	\rm -f $(MAIN).ps $(MAIN).pdf
	\rm -rf TST
	\rm -f all.tar


all.tar:
	tar cvfh all.tar makefile $(MAIN).tex $(TEXPARTS) $(BIBPARTS) \
	$(FIGPARTS) README 

