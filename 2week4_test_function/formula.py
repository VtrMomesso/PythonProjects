
class FormulaError(ValueError):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O to [["H", 2], ["O", 1]] and 
    "PO4H2(CH2)12CH3" to [["P', 1], ["O", 4], ["H", 29], ["C", 13]]
    
    Parameters:
        formula: is a string that contains a chemical formula.
        periodic_table_dict: is the compound dictionary returned
            from make_periodic_table.
    Return: a compound list that contains chemical symbol and
        quantities like  this [["Fe", 2], ["O", 3]]
    """