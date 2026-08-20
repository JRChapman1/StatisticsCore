import numpy as np
from src.statistics_core.processes.PoissonProcess import PoissonProcess

print("Testing PoissonProcess...")

try:
    pp = PoissonProcess(rate=2.0, step_size=0.1)
    print("✓ PoissonProcess created successfully")
    
    result = pp.simulate(num_steps=10, num_sims=1)
    print("✓ Simulation successful!")
    print("Result shape:", result.shape)
    print("Result:\n", result)
    
except AttributeError as e:
    print(f"✗ AttributeError: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"✗ Error ({type(e).__name__}): {e}")
    import traceback
    traceback.print_exc()

