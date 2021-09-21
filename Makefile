ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	@for path in c cpp cython elixir golang node pypy3 pypy2 python ruby rust; do \
		echo "Running '$$path'"; \
		cd $$path; \
		make run; \
		echo "========================"; \
		cd $(ROOT_DIR); \
	done

clean:
	@for path in c cpp cython elixir golang node pypy3 pypy2 python ruby rust; do \
		echo "Cleaning '$$path'"; \
		cd $$path; \
		rm -f output.txt; \
		cd $(ROOT_DIR); \
	done

chart: run
	@pip install plotly dash
	@python3 app.py