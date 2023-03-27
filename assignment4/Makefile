N = 500000

all: clean compile run extra2 extra4 end

compile:
	javac *.java

run:
	python test_n_d.py

extra2:
	python extra2.py

extra4:
	python extra4.py

end:
	rm -rf *.class


clean:
	git clean -Xdf