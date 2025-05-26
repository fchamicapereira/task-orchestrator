#!/usr/bin/env python3


from TaskOrchestrator.orchestrator import Orchestrator, Task
from pathlib import Path

import os


if __name__ == "__main__":
    print(f"Process ID: {os.getpid()}")
    print("Press Ctrl+C to interrupt the task...")

    o = Orchestrator()

    o.add_task(Task("task1", "sleep 100000"))

    o.visualize(dot_file=Path(__file__).parent / "orchestrator_example_interrupt.dot")
    o.run()
