import pandas as pd

class Factors():

    def __init__(self, probabilities):

        """
        maybe it can represent the values from the
        dictionary since it is of type panda
        """

        self.probabilities = probabilities

    def remove_factor(self, node, node_val):

        # this keeps only the rows which have the value we need for the probability
        # from drop onwards -> this then drops the column of that variable / node
        updated_factor = self.probabilities[self.probabilities[node] == node_val].drop([node], axis = 1)

        return updated_factor

    def sum_rows(self, node):

        """
        This function is the last step before I update the sum
        It takes place after the product, and it sums up all the rows
        such that I can then remove the variable
        """

        other_columns = [col for col in self.probabilities if col != node]
        data_without_the_node = self.probabilities.groupby(other_columns).sum()

        return data_without_the_node

    def factor_product(self, args):

        factor_number = len(args)

        # the constructor will need to be change
        for i, j in zip(range(factor_number), range(factor_number - 1)):
            factor_1 = args[i]
            factor_2 = args[j]






