# iterative Approach 

def fib(n):
  """Calculates the nth Fibonacci number."""
  if n < 0:
    raise Exception("Input n must be non-negative")
  elif n == 0 or n == 1:
    return n
  else:
    a = 0
    b = 1
    for  _ in range(2, n + 1):
      c = a + b
      a = b
      b = c
    return c


def fib_step_count(n):
  """Calculates the number of steps required to calculate the nth Fibonacci number using the iterative approach."""
  if n < 0:
    raise Exception("Input n must be non-negative")
  elif n == 0 or n == 1:
    return 1
  else:
    a = 0
    b = 1
    step_count = 2  # Start with 2 steps for n=2
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
        step_count += 3
    return step_count


# Example usage:

if __name__ == "__main__":
  num = int(input("Enter Number : "))
  print(f"Fibonacci({num}) = {fib(num)}")
  print(f"Total step count: {fib_step_count(num)}")


'''
Enter Number : 6
Fibonacci(6) = 8
Total step count: 17
'''
