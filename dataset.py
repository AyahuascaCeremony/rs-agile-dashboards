class DataSet:
  def __init__(self, name, p_pts, p_pts_c, up_pts, up_pts_c):
    self.name = name
    self.planned_points = p_pts
    self.planned_points_completed = p_pts_c
    self.planned_points_not_completed = p_pts - p_pts_c
    self.unplanned_points = up_pts
    self.unplanned_points_completed = up_pts_c
    self.unplanned_points_not_completed = up_pts - up_pts_c

  def __str__(self):
    completed_total = self.planned_points_completed + self.unplanned_points_completed
    total = self.planned_points + self.unplanned_points
    return "Sprint " +  self.name + " saw " + str(completed_total) + " completed out of " + str(total)