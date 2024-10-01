def vacuum_cleaner_agent(location, status):
  if status[location] == 'Dirty':
    return f"The vacuum cleaner is in location {location} and it is dirty. Cleaning location {location}."
  else:
    if location == 'A':
      return f"The vacuum cleaner is in location {location} and it is clean. Moving to location B."
    else:
      return f"The vacuum cleaner is in location {location} and it is clean. Moving to location A."

location = 'A'
status = {'A': 'Dirty', 'B': 'Dirty'}

while True:
  action = vacuum_cleaner_agent(location, status)
  print(action)

  if status[location] == 'Dirty':
    status[location] = 'Clean'

  if location == 'A':
    location = 'B'
  else:
    location = 'A'

  if status['A'] == 'Clean' and status['B'] == 'Clean':
    print("Both locations are clean. The vacuum cleaner is finished.")
    break
