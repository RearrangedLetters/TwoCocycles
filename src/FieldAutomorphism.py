class FieldAutomorphism:

    ###
    # @base is the base for which the automorphism is defined
    # @functions is a list of #base many functions where each function
    # describes the behaviour of the automorphism on the respective
    # coordinate.
    def __init__(self, base, automorphism):
        self.base = base
        self.automorphism = automorphism

    def apply(self, vector):
        return self.automorphism(vector)
