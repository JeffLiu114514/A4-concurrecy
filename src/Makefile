N = 100

all: clean compile run end

compile:
	javac *.java

run:
	python test.py $(N)

end:
	rm -rf *.class


clean:
	git clean -Xdf