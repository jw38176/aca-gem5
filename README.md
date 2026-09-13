Intended workflow:
students run simulate.py with specified CPU paramteres. This launches gem5 running the bzip2 program. This then runs gem5tomcpat.py on the output stats file, then launches mcpat with the generated input to attain the power usage.

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

Run a simulation:

```
python simulate.py
```

Use `--help` to see available configuration options.
