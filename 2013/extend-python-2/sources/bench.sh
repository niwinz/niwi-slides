#!/bin/sh


echo "CFFI"
python -m timeit -s "import bench_cffi as s" "s.gcd(100, 662)"
echo "CTYPES"
python -m timeit -s "import bench_ctypes as s" "s.gcd(100, 662)"

