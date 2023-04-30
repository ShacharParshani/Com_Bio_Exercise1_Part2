def probability_to_spread(s_level):  # Probability of spreading the rumor
    if s_level == 1 or s_level == 0:  # 0 for the case that the level of skepticism temporarily decreased by one
        return 1
    if s_level == 2:
        return 2 / 3
    if s_level == 3:
        return 1 / 3
    if s_level == 4:
        return 0


class Person:
    def __init__(self, s):
        self.s = s  # level of skepticism. valid - 1,2,3,4
        self.gen = -1  # the generation of hearing the rumor. -1 no hearing
        self.count_get = 0  # count how many times this person got the rumor in the current generation
        self.pre_count_get = 0  # like count_get, for the previous generation
        self.prevent = 0  # 0 if the person is not prevented from spreading the rumor,
        # otherwise - the last generation he spreeded
        # which generation the person spreaded the rumor
