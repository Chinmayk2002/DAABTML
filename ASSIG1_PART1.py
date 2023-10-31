def fib(n):
  """Calculates the nth Fibonacci number."""
  if n < 0:
    raise Exception(f"Input {n} must be non-negative")
  elif n == 0 or n == 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)


def fib_step_count(n):
  """Calculates the number of steps required to calculate the nth Fibonacci number using the recursive approach."""
  if n < 0:
    raise Exception(f"Input {n} must be non-negative")
  elif n == 0 or n == 1:
    return 1
  else:
    return fib_step_count(n - 1) + fib_step_count(n - 2) + 1


# Example usage:
if __name__ == "__main__":
  num = int(input("Enter Number : "))
  print(f"Fibonacci({num}) = {fib(num)}")
  print(f"Total step count: {fib_step_count(num)}")


'''
Enter Number : 6
Fibonacci(6) = 8
Total step count: 25
'''
  


