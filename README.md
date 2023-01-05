# Advent of Code 2022

Last year I had a go at the [Advent of Code](https://adventofcode.com/) but ran out of time in the last week and didn't finish it.

This year I'm having another go, mostly using Python since it feels like the right language for this sort of problem.
After working it out in Python, I'm then trying the same thing in Julia. I am almost completely unfamiliar with this
language so I don't expect the code to be high quality or efficient but I'll be happy if I can get it to give the
correct answer and not just look like a carbon copy of the Python code.

Originally I was using CPython 3.10, which was what was installed on my laptop. When some early un-optimized problems
started taking hours to run, I looked at alternatives. It turned out that 3.11 ran about 30% faster but PyPy was
faster still, about 8x faster.

I have been trying to just use 'plain' python and not install any 3rd party libraries. The only exception is numpy,
which came in handy when dealing with matrices and multi-dimensional arrays.

If I get chance, I'll go back and try to finish off 2021.