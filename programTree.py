import sys
import programStats

class ProgramTree:
  def __init__(self):
    self.children = []
    self.programText = None
    self.programStats = None

if __name__ == "__main__":
    root = ProgramTree()
    root.programStats = programStats.ProgramStats()