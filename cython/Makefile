build: loop.pyx
	@pip install easycython
	@easycython loop.pyx

run: build
	@python main.py

clean:
	@rm -f output.txt