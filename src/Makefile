
all: clean compile run run2 run3 run4 extra2 end

compile:
	javac *.java

run:
	python run.py

run2:
	python run_bigN.py

run3:
	python run_deep.py

run4:
	python run_deep_largeN.py

extra2:
	python extra2.py


end:
	rm -rf *.class


clean:
	git clean -Xdf