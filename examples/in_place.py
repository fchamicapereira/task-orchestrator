#!/usr/bin/env python3

from TaskOrchestrator.orchestrator import Orchestrator, Task
from pathlib import Path

if __name__ == "__main__":
    o = Orchestrator(
        [
            Task(
                "task1",
                "true",
                next=[
                    Task("task2", "true"),
                ],
            ),
            Task(
                "task3",
                "true",
                next=[
                    Task("task2", "true"),
                    Task("task4", "true"),
                    Task("task5", "true"),
                ],
            ),
        ],
    )

    o.visualize(dot_file=Path("/tmp/orchestrator_example_in_place.dot"))
    o.run()
