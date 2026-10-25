def benchmarking(func, *args):
    start_time = time.perf_counter()
    cpu_start = time.process_time()
    result = func(*args)
    cpu_end = time.process_time()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    execution_time_ms = elapsed_time * 1000
    cpu_usage = ((cpu_end - cpu_start) / elapsed_time * 100) if elapsed_time else 0.0

    print(f"Simulation Time: {execution_time_ms:.5f} ms")
    print(f"CPU Utilization: {cpu_usage}%")

    return result, execution_time_ms, cpu_usage