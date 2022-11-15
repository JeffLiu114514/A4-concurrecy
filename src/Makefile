N = 100

all: clean compile extra end

compile:
	javac *.java

run:
	python test.py $(N)

extra:
	python extra.py

end:
	rm -rf *.class


clean:
	git clean -Xdf