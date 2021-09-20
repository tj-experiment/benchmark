ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	@for path in c cpp cython elixir golang python ruby rust node; do \
		echo "Running '$$path'"; \
		cd $$path; \
		make run; \
		echo "========================"; \
		cd $(ROOT_DIR); \
	done

clean:
	@for path in c cpp cython elixir golang python ruby rust node; do \
		echo "Cleaning '$$path'"; \
		cd $$path; \
		rm -f output.txt; \
		cd $(ROOT_DIR); \
	done

chart:
	pip install plotly
	python3 chart.py