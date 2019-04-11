from dataset import DataSet

datasets = []

while True:
  name = raw_input("Name your sprint:")
  if name == "q":
    break

  planned_points = int(input("How many points did you plan to do?"))
  planned_points_completed = int(input("How many of them did you complete?"))
  unplanned_points = int(input("How many points did you introduce after planning?"))
  unplanned_points_completed = int(input("And, how many of them did you complete?"))

  dataset = DataSet(name, planned_points,

  planned_points_completed, unplanned_points, unplanned_points_completed)
  datasets.append(dataset)

for data in datasets:
  print data