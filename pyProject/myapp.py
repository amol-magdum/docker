def save_and_show_user_input(filename):
  """Saves user input to a text file and shows the content.

  Args:
    filename: The name of the text file to save the input to.
  """

  user_inputs = []
  while True:
    user_input = input("Enter your input (or 'q' to quit): ")
    if user_input.lower() == 'q':
      break
    user_inputs.append(user_input + '\n')

  with open(filename, 'a') as file:
    file.writelines(user_inputs)

  show_info = input("Do you want to see all user names y/n: ")
  if show_info == 'y':
        with open(filename, 'r') as file:
            print("Saved content:")
            print(file.read())

if __name__ == '__main__':
#   filename = input("Enter the filename to save the input (e.g., input.txt): ")
  save_and_show_user_input("input.txt")
