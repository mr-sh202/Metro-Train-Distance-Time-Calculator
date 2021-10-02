from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.tz import tzlocal
from datetime import datetime, timedelta

class Task(TaskTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.timer_1_tick()

  def timer_1_tick(self, **event_args):
    """Every second, update the live countdown on this task."""
    start_time = self.item[1].replace(tzinfo=tzlocal())
    end_time = self.item[1].replace(tzinfo=tzlocal()) + timedelta(minutes=self.item[0]['duration_mins'])
    
    time_until_start = start_time - datetime.now(tzlocal())
    time_until_end = end_time - datetime.now(tzlocal())
    
    if time_until_start.total_seconds() > 0:
      self.live_time.text = "Starts in %.0f minutes" % (time_until_start.total_seconds() / 60)
      self.in_progress.visible = False
    elif time_until_end.total_seconds() > 0:
      self.live_time.text = "%.0f minutes remaining" % (time_until_end.total_seconds() / 60)
      self.in_progress.visible = True
    else:
      self.live_time.text = "Finished %.0f minutes ago." % ((-time_until_end).total_seconds() / 60)
      self.in_progress.visible = False
      self.foreground = "#aaa"

