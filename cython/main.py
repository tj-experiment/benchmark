import loop

elapsed = loop.loop()

with open('output.txt', 'a+') as f:
    f.write("%s\n" % elapsed)