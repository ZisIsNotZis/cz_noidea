# cz_noidea

**One-line:** A flat personal scratchpad of ~37 Jupyter notebooks and 3 Python scripts used to poke at CPython/`asyncio`/NumPy/PyTorch internals and benchmark throughput.

**Why it exists:** Working notebook for one-off "what does this do / how fast is it" questions — `asyncio` task/IPC throughput, `pynng` and raw-socket benchmarks, a hand-rolled sparse-array prototype, NumPy float bit-twiddling and entropy measures, `numba` GEMM kernels, `fastai`/`torch` loss-index experiments, and a `pyspark` correlation detour. Nothing here is a library or an app; it is the raw bench.

**How to run:** Not runnable as a package. There is no entrypoint, no test, no manifest. Individual notebooks assumed a Python **3.8** Jupyter kernel (metadata: 3.8.5 / 3.8.6, one 3.9.0) with `numpy`, `numba`, `torch`, `fastai`, `pynng`, `uvloop`, `aiohttp`, `pandas`, `pyspark`, `plotly`, `matplotlib`, `Pillow`, `flask` installed ad hoc. Several cells reference host-local scratch paths (`/datb/...`) and one script shebang points at an internal conda env.

**Status:** **Deprecated (2020–2021 era) — kept as an archive.** Signals: Python 3.8 kernels, `fastai.vision.all`, `np.math.*` (removed in NumPy 2), `from asyncio import coroutine`, bare `get_event_loop()`, `loop.add_reader`, and a `torch` loss-index hack tied to an old fastai version. This is preserved as an honest record of exploratory work, not as something to build on.

**License:** See `LICENSE` for this repository's AGPL-3.0 license. The embedded Apache Spark README in `spark.ipynb` is third-party Apache-2.0 content; review its attribution and redistribution terms before publishing a derivative.

---
