###
# Returns the automorphism x ↦ phi(psi(x))
###
def composite(phi, psi):
    comp = list()
    for i, p in enumerate(phi):
        comp.append(lambda x: p(psi[i](x)))
    return comp


class FieldAutomorphism:

    ###
    # @base is the base for which the automorphism is defined
    # @functions is a list of #base many functions where each function
    # describes the behaviour of the automorphism on the respective
    # coordinate.
    ###
    def __init__(self, base, automorphism):
        self.base = base
        self.automorphism = automorphism

    def apply(self, vector):
        trans_vector = list()
        for i, phi in enumerate(self.automorphism):
            trans_vector.append(phi(vector[i]))
        return trans_vector

    ###
    # Returns the automorphism x ↦ self(psi(x))
    ###
    def composite(self, psi):
        return composite(self.automorphism, psi)
