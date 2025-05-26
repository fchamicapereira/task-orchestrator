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
                    Task(
                        "task2",
                        "false",
                        next=[
                            Task("task3", "true"),
                        ],
                    ),
                ],
            ),
        ],
    )

    o.visualize(dot_file=Path(__file__).parent / "failed.dot")
    o.run()
