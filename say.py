import cowsay
import sys
import sayings

from sayings import goodbye

if len(sys.argv) == 2:
    cowsay.dragon("Hello, " + sys.argv[1])
    
goodbye("Eka")
sayings.hello("Eka")