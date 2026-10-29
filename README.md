# Repository environment

This repository currently contains only the text file `wdwdwd`. There is no
application, dependency installation, build pipeline, or long-running service.
Consequently, the Aether environment intentionally declares no preview terminals.

## Setup

Run from the repository root:

```sh
python3 --version
```

Python 3 is the only prerequisite. Setup checks its availability, is safe to
repeat, and requires no secrets. No per-boot or Docker preparation is needed.

## Verification

Run the dependency-free environment smoke tests:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

These check that the environment configuration is valid, declares the documented
setup command, and does not declare nonexistent application services. They do not
test application functionality: no application exists yet. When one is added,
update this documentation and `.aether/environment.json` with its canonical setup
and development commands, then verify its declared ports with local HTTP probes.
