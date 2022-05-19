import spawningtool
from spawningtool.parser import GameTimeline

class SpawningReplayModel():
 
  def loadRequestedReplay(self, filePath):
    result_replay = spawningtool.parser.parse_replay(filePath)
    return result_replay