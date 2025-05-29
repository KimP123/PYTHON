import time

def print_first_element(n):
    sample_list = list(range(1, n + 1))

    start_time = time.time()

    if sample_list:
        print("The first element is:", sample_list[0])
    else:
        print("The list is empty.")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.10f} seconds")

try:
    n = int(input("Enter a value for n: "))
    print_first_element(n)
except ValueError:
    print("Please enter a valid integer.")