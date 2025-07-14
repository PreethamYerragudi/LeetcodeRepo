class Solution(object):

    def matchPlayersAndTrainers(self, players, trainers):
        """
      :type players: List[int]
      :type trainers: List[int]
      :rtype: int
      """
        trainers.sort()
        players.sort()
        ans = 0
        pointer = 0
        for player in players:
            while pointer < len(trainers) and trainers[pointer] < player:
                pointer += 1
            if pointer < len(trainers):
                ans += 1
                pointer += 1
        return ans
