run:
	@for path in c cpp cython elixir golang node pypy3 pypy2 python ruby rust scala; do \
		echo "Running '$$path'"; \=
		make -C $$path run; \
		echo "========================"; \
	done

clean:
	@for path in c cpp cython elixir golang node pypy3 pypy2 python ruby rust scala; do \
		echo "Cleaning '$$path'"; \
		make -C $$path clean; \
	done

chart: run
	@pip install plotly dash
	@python3 app.py
