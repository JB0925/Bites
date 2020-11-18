scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None


    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for i in range(len(scores)):
            color = BELTS.get(scores[i])
            if scores[i] != max(scores):
                if scores[i] <= new_score < scores[i+1]:
                    if self._last_earned_belt != color:
                        self._last_earned_belt = color
                        return True

            else:
                if scores[i] == max(scores) and new_score >= max(scores):
                    if self._last_earned_belt != color and self._last_earned_belt != ranks[i]:
                        self._last_earned_belt = color
                        return True
        
        return False
            

    def _get_score(self):
        return self._score


    def _set_score(self, new_score: int):
        if not isinstance(new_score, int):
            raise ValueError ('Score must be an int')
        if new_score < self._score:
            raise ValueError ('Score cannot be lower than the previous score')

        if self._get_belt(new_score):      
            belt = self._last_earned_belt.title()
            print(f'Congrats, you earned {new_score} points obtaining the PyBites Ninja {belt} Belt')
        else:
            print(f'Set new score to {new_score}')
        
        self._score = new_score

    score = property(_get_score, _set_score)


ninja = NinjaBelt()

ninja.score = 10
ninja.score = 49