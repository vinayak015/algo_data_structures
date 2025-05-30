"""
You are given an integer array matches where matches[i] = [winner_i, loser_i] indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matches_lost = {}
        zero_loss = set()
        one_loss = set()

        for winner, looser in matches:
            zero_loss.add(winner)

            if looser not in matches_lost:
                matches_lost[looser] = 1
            else:
                matches_lost[looser] += 1

            if winner not in matches_lost:
                matches_lost[winner] = 0

            if matches_lost[winner] > 0:
                if winner in zero_loss:
                    zero_loss.remove(winner)

            if looser in zero_loss and matches_lost[looser] > 0:
                zero_loss.remove(looser)

            if matches_lost[looser] > 1:
                if looser in one_loss:
                    one_loss.remove(looser)
            elif matches_lost[looser] == 1:
                one_loss.add(looser)

        return [sorted(list(zero_loss)), sorted(list(one_loss))]

    def findWinners_(self, matches: List[List[int]]) -> List[List[int]]:
        lost_matches = {}
        seen = set()

        for winner, looser in matches:
            seen.add(winner)
            seen.add(looser)
            lost_matches[looser] = lost_matches.get(looser, 0 ) + 1

        zero_loss, one_loss = [], []
        for player in seen:
            if player not in lost_matches:
                zero_loss.append(player)
            if player in lost_matches and lost_matches[player] == 1:
                one_loss.append(player)
        return [sorted(zero_loss), sorted(one_loss)]





if __name__ == "__main__":
    sol = Solution()
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    # matches = [[2,3],[1,3],[5,4],[6,4]]
    # matches = [[26651,85186],[19790,34845],[20238,59388],[12788,40994],[46703,28184],[49936,83960],[76158,33038],[96005,2100],[86989,72152],[73342,82931],[90852,54532],[61649,18655],[9506,73692],[56189,5503],[34939,78765],[98315,19818],[57974,42491],[5906,8266],[97215,95437],[48266,87323],[86578,82992],[29919,70323],[38749,98079],[10259,27750],[977,39147],[43625,38229],[56044,32634],[53509,13100],[59446,68045],[38379,7712],[87511,62110],[35456,508],[76381,89490],[73270,55169],[82004,20887],[11239,24195],[56561,57161],[96112,81582],[20403,76188],[77876,61782],[99546,39653],[68650,57489],[27952,11410],[10595,73394],[98154,49624],[10866,3758],[70902,97205],[43360,93218],[59119,82709],[7379,47660],[76950,1884],[20120,87138],[23010,5729],[96553,12208],[70423,36052],[98588,30989],[87447,24694],[90748,39031],[17455,13250],[49557,4501],[99624,72185],[24791,99744],[80458,57635],[16175,29359],[53170,83581],[95936,39348],[5634,95357],[58517,73348],[54861,34521],[86692,23939],[11623,85398],[7562,4748],[13217,29610],[52705,67263],[95277,68332],[50498,96263],[18070,33256],[1901,4237],[11894,97936],[22135,34362],[7698,64698],[22893,62847],[2294,14712],[69996,48778],[340,93723],[42138,33976],[53231,33755],[29512,501],[81773,58971],[19189,20321],[30220,37726],[78678,17938],[79172,26444],[67695,39219],[23206,40923],[5651,8928],[49333,29553],[98589,75052],[99636,94502],[38455,66022],[3654,56685],[42118,65465],[83831,62461],[81301,90996],[35209,23863],[99223,69931],[5206,42971],[2143,97501],[91454,60002],[6307,70975],[48194,6557],[60125,70237],[60551,85062],[58731,86177],[98064,94854],[63923,51970],[87687,36064],[37926,97759],[87685,22212],[62051,7149],[1430,13255],[55928,48428],[8319,99922],[58503,69220],[45821,70178],[56815,31101],[77963,7364],[28828,65658],[92037,99306],[97928,41984],[47086,73658],[35491,79727],[24688,42610],[32304,18289],[52770,31966],[96613,96122],[73643,49573],[27623,89143],[62163,93629],[41018,53285],[59655,4055],[80777,17295],[9744,38601]]
    print(sol.findWinners_(matches=matches))


