all:    
	chmod a+rwx `pwd`
	python gm_main.py --file `pwd`/samplegraph.txt --dest_dir `pwd`/output --belief_file `pwd`/priorsbelief.txt --unweighted --undirected
	
plot:
	sh plot/generatePlots.sh

paper.pdf: doc/paper.tex
	cd doc; make
	
install:
	sudo apt-get install python-psycopg2

all.tar:
	tar -zcvf graphminer.tar.gz *.txt makefile *.py matlab output doc img dataset plot unit-test

clean:
	rm *.pyc


