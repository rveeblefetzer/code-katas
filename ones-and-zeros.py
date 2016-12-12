def binary_array_to_number(arr):
  """Given list of 1s and 0s, convert equivalent binary value to an integer."""
  in_string = []
  for num in arr:
     in_string.append(str(num))
  in_string = "".join(in_string)
  return int(in_string, 2)
