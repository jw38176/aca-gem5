import subprocess
import psutil
import time
import argparse

parser = argparse.ArgumentParser(description="Sweep Reorder Buffer size and Integer Physical Register count, using multiple CPU cores.")
parser.add_argument("--max-cpu", type=int, default=8,
                    help="Maximum number of concurrent gem5 simulations (defaults is 8)")
args = parser.parse_args()
max_cpu = max(1, args.max_cpu)

# Define parameters
rob_sizes = [16, 32, 64, 128, 256]
int_reg_sizes = [49, 62, 75, 88, 101]

processes = []  

def _throttle_processes():
    global processes
    # Remove finished processes
    processes = [p for p in processes if p.poll() is None]
    while len(processes) >= max_cpu:
        # Block on the first process in the list
        processes[0].wait()
        # Clean up any finished processes
        processes = [p for p in processes if p.poll() is None]

for rob_size in rob_sizes:
    for int_reg_size in int_reg_sizes:
        
        name = f"rob_{rob_size}_intregs_{int_reg_size}"

        cmd = (
            "python /homes/jkw20/aca-gem5/simulate.py "
            f"--rob-size {rob_size} "
            f"--num-int-phys-regs {int_reg_size} "
            f"--name {name}"
        )
        # Launch the simulation
        processes.append(subprocess.Popen(cmd, shell=True))
        _throttle_processes()

for p in processes:
    p.wait()

