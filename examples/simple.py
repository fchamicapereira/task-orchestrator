#!/usr/bin/env python3

from TaskOrchestrator.orchestrator import Orchestrator, Task
from pathlib import Path

if __name__ == "__main__":
    o = Orchestrator()

    o.add_task(Task("task1", "touch /tmp/B", files_produced=["/tmp/B"]))
    o.add_task(Task("task2", "touch /tmp/D", files_produced=["/tmp/D"]))
    o.add_task(Task("task3", "touch /tmp/C", files_consumed=["/tmp/B", "/tmp/D"], files_produced=["/tmp/C"]))

    o.visualize(dot_file=Path(__file__).parent / "simple.dot")
    o.run()
