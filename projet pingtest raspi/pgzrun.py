#COPY THIS IN \Lib\site-packages OTHERWISE YOU CANNOT RUN IT FROM TERMINAL
import sys
import os
from pgzero.runner import prepare_mod, run_mod


mod = sys.modules['__main__']
if not getattr(sys, '_pgzrun', None):
    if not getattr(mod, '__file__', None):
        
        prepare_mod(mod)


def go():
    """Run the __main__ module as a Pygame Zero script."""
    if getattr(sys, '_pgzrun', None):
        return

    run_mod(mod)
