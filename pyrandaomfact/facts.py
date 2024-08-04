import requests

def fetch_random_dog_fact():
  """Fetches a random dog fact from the Dog API.

  Returns:
    A string containing the retrieved dog fact, or None if an error occurs.
  """

  api_url = "https://dogapi.dog/api/v2/facts?limit=1"

  try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    fact = data["data"][0]["attributes"]["body"]
    return fact

  except requests.exceptions.RequestException as e:
    print(f"Error fetching dog fact: {e}")
    return None

if __name__ == "__main__":
  dog_fact = fetch_random_dog_fact()
  if dog_fact:
    print(dog_fact)
  else:
    print("Failed to retrieve a dog fact.")
