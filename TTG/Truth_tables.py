# negation: 'not', '-', '~'
# logical disjunction: 'or'
# logical nor: 'nor'
# exclusive disjunction: 'xor', '!='
# logical conjunction: 'and'
# logical NAND: 'nand'
# material implication: '=>', 'implies'
# logical biconditional: '='
from ttg import ttg

if __name__ == '__main__':
    # print(ttg.Truths(['p', 'q'], ['p and q', 'p or q', '(p or (~q)) => (~p)']))

    table_val = ttg.Truths(['p', 'q'], ['p = q', 'p and (~p)', '(p and q) => p'])
    print(table_val)
    print(table_val.valuation(4))
