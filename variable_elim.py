"""
@Author: Joris van Vugt, Moira Berens, Leonieke van den Bulk

Class for the implementation of the variable elimination algorithm.

"""
from Demos.SystemParametersInfo import new_h

import read_bayesnet as ReadBayesnet

class VariableElimination():

    def __init__(self, network):
        """
        Initialize the variable elimination algorithm with the specified network.
        Add more initializations if necessary.

        """
        self.network = network


    def run(self, query, observed, elim_order):
        """
        Use the variable elimination algorithm to find out the probability
        distribution of the query variable given the observed variables

        Input:
            query:      The query variable
            observed:   A dictionary of the observed variables {variable: value}
            elim_order: Either a list specifying the elimination ordering
                        or a function that will determine an elimination ordering
                        given the network during the run

        Output: A variable holding the probability distribution
                for the query variable

        """
        pass

    def adjust_elimation_order(self, elim_order, query):
        if query in elim_order:
            elim_order.remove(query)

        leaf_nodes = []

        for key, value in self.network.parents:
            if len(value) == 0:
                leaf_nodes.append(key)

        new_elimination_order = []
        new_elimination_order.append(leaf_node for leaf_node in leaf_nodes)
        new_elimination_order.append(elem for elem in elim_order if elem not in new_elimination_order)

        # suggested by PyCharm, does not work - fix it if you feel like doing it
        # new_elimination_oder = [leaf_node for leaf_node in leaf_nodes, elem for elem in elim_oder if
        #                         elem not in new_elimination_oder]

        return new_elimination_order

    def create_factors(self):

        #TODO: THIS MAY NEED TO BE UPDATED, SPECIFICALLY THE ARGUMENTS

        sum_factors = []

        for key, value in self.network.parents:
            if len(value) == 0:
                sum_factors.append(key)

            else:
                temp = value
                temp.append(key)
                sum_factors.extend(temp)

        return sum_factors

    def factors_multiplication(self, factors):
        # result = factors[0]
        #
        # for factor in factors:

        pass



