# 1. Write a program to find first of all non terminals in a grammar
# 2. Write a program to find follow of all non terminals in a grammar
 
"""

    Epsilon is represented by #.
    Productions are of the form A=B, where ‘A’ is a single Non-Terminal and ‘B’ can be any combination of Terminals and Non- Terminals.
    Grammer is not left recursive.
    Terminals with only single characters work, example a terminal as 'abc' WONT work 
    DO NOT use the same char for terminal and non terminal
    Do not use ‘#’ or ‘$’ as they are reserved for special purposes.

"""



import sys
import re
sys.setrecursionlimit(60)


def First(string):
    #print("first({})".format(string))
    first_ = set()
    if string in nonterminals:
        alternatives = production_dict[string]

        for alternative in alternatives:
            first_2 = First(alternative)
            first_ = first_ | first_2

    elif string in terminals:
        first_ = {string}

    elif string == '' or string == '#':
        first_ = {'#'}

    else:
        first_2 = First(string[0])
        if '#' in first_2:
            i = 1
            while '#' in first_2:
                

                first_ = first_ | (first_2 - {'@'})
                
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = First(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2

    
    return first_


def Follow(nT):
    
    follow_ = set()
    
    prods = production_dict.items()
    if nT == start_symbol:
        follow_ = follow_ | {'$'}
    for nt, rhs in prods:
        
        for alt in rhs:
            for char in alt:
                if char == nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str == '':
                        if nt == nT:
                            continue
                        else:
                            follow_ = follow_ | Follow(nt)
                    else:
                        follow_2 = First(following_str)
                        if '#' in follow_2:
                            follow_ = follow_ | follow_2-{'#'}
                            follow_ = follow_ | Follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    
    return follow_


print("\nASSUMPTIONS: \n\nEpsilon is represented by  # .\nProductions are of the form A=B, where ‘A’ is a single Non-Terminal and ‘B’ can be any combination of Terminals and Non - Terminals.\nGrammer is not left recursive.\nTerminals with only single characters work, example a terminal as 'abc' WONT work.\nDO NOT use the same char for terminal and non terminal.\nDo not use   # or $ as they are reserved for special purposes.\n\n")

number_of_terminals = int(input("Enter the number of terminals : "))
terminals = []
print("Enter the terminals : ")
for i in range(number_of_terminals):
    terminals.append(input())

number_of_nonterminals = int(input("Enter the number of non terminals : "))
nonterminals = []
print("Enter the non terminals : ")
for j in range(number_of_nonterminals):
    nonterminals.append(input())

start_symbol = input("Enter the start symbol : ")
production_count = int(input("Enter the number of productions : "))
productions = []
print("Enter the productions : ")
for k in range(production_count):
    productions.append(input())

# input testing --------(remove while cleaning)
print("terminals : ",terminals)
print("non terminals : ",nonterminals)
print("productions : ",productions)

# enable the dict to hold lists
production_dict = {}
for nt in nonterminals:
    production_dict[nt] = []

# split the productions into parts to simplify parsing
for production in productions:
    nonterminal_to_production = production.split("->")
    expanded = nonterminal_to_production[1].split("/") # assumption : single char terminals
    for ex in expanded:
        production_dict[nonterminal_to_production[0]].append(ex)


# -----(remove while cleaning)
print("production_dict",production_dict)

# declare dicts for first and follow as they are set of elements mapped to keys(non terminals)
FIRST = {}
FOLLOW = {}

for nonterminal in nonterminals:
    FIRST[nonterminal] = set()
    FOLLOW[nonterminal] = set()

for nonterminal in nonterminals:
    FIRST[nonterminal] = FIRST[nonterminal] | First(nonterminal)

FOLLOW[start_symbol]=FOLLOW[start_symbol] | {'$'}
for non_terminal in nonterminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | Follow(non_terminal)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals', 'First', 'Follow'))
for non_terminal in nonterminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal, str(
        FIRST[non_terminal]), str(FOLLOW[non_terminal])))

