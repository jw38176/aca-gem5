Intended workflow:
students run simulate.py with specified CPU paramteres. This launches Gem5 running the gapbs tc benchmark. This then runs gem5tomcpat.py on the output stats file, then launches mcpat with the generated input to attain the power usage.

Build gem5:

```
cd gem5
scons build/X86/gem5.fast --with-lto -j 8
```

Build mcpat:

```
cd mcpat
make -j 8
```

Build gapbs

```
cd benchmarks/gapbs
make -j 8
```

Test tc:

`./tc -u 10 -n 1 -k 16`

This specifies the number of verticies (2^n), number of iterations and the vertex degree. The original benchmark generates a random graph every time, whereas the one in this repo has been modified to generate the same graph every time.

Run a simulation:

```
python simulate.py
```

Use `--help` to see available configuration options.
