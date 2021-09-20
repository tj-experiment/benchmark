

defmodule Main do
  @size 10000000
  def main do
    Enum.each(1..@size, fn number -> number end)
  end
end

{microseconds, :ok} = :timer.tc(Main, :main, [])

elapsed = microseconds/1000

IO.puts("Took #{elapsed} milliseconds")

{:ok, file} = File.open("output.txt", [:append])

IO.binwrite(file, "#{elapsed}\n")

File.close(file)
