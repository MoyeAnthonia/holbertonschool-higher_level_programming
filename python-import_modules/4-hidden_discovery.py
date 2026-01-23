#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(*sorted(n for n in dir(mod) if not n.startswith("__")), sep="\n")
