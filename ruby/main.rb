def main()
    starting = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    for i in 0..10_000_000 do
       next
    end
    ending = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    elapsed = (ending - starting) * 1000.0
    puts "Took %d milliseconds" % [elapsed]

    open('output.txt', 'a') do |f|
      f << elapsed << "\n"
    end
end

main