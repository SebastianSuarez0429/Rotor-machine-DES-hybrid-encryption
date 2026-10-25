import os
import time

def rotor_cipher(text: str, key: tuple[int, int, int], decrypt=False) -> str:
    r1, r2, r3 = key
    result = []
    for char in text.upper():
        if not char.isalpha():
            result.append(char)
            continue

        # Step rotors
        r1 = (r1 + 1) % 26 # Step the first rotor Example: r1 increments with each character if it were 24
        # Then it would be 25 then 26 and wrap around to 0 which triggers the next rotor to step
        if r1 == 0:
            r2 = (r2 + 1) % 26 # It does the same as the first rotor, stepping with each full rotation of the previous rotor
            if r2 == 0:
                r3 = (r3 + 1) % 26 # Finally, the third rotor steps with each full rotation of the second rotor

        #Making these step rotors be 26x26x26 ensures that the total shift covers all possible combinations of rotor positions


        total_shift = r1 + r2 + r3 #this gives the combined shift from all three rotors (Like caesar cipher kinda)
        val = ord(char) - ord('A') # Convert character to 0-25 range for shifting
        if decrypt:
            val = (val - total_shift) % 26 # Shift the character backwards for decryption
        else:
            val = (val + total_shift) % 26 # Shift the character forwards for encryption
        result.append(chr(val + ord('A'))) #Add them into the list

    return "".join(result) #Format time!

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

encrypted = rotor_cipher("NEW YEAR", (5, 2, 7))
print("Encrypted:", encrypted)
print("------------------------------------------------")
print("Decrypted:", rotor_cipher(encrypted, (5, 2, 7), decrypt=True))
print("------------------------------------------------")
print(benchmarking(rotor_cipher, "NEW YEAR", (5, 2, 7)))
