# 1-index
a, b, c, d = 1, 2, 3, 4
e, f, g, h = 5, 6, 7, 8
i, j, k, l = 9, 10, 11, 12

# dict of variables

# 0-index
a, b, c, d = 0, 1, 2, 3
e, f, g, h = 4, 5, 6, 7
i, j, k, l = 8, 9, 10, 11



# String values of variables
a, b, c, d = "a", "b", "c", "d"
e, f, g, h = "e", "f", "g", "h"
i, j, k, l = "i", "j", "k", "l"

# dict of variables
graph_of_variables = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
    "e": [],
    "f": [],
    "g": [],
    "h": [],
    "i": [],
    }
# example of how to use graph_of_variables
graph_of_variables["a"].append("b")
graph_of_variables["a"].append("c")
graph_of_variables["a"].append("d")
graph_of_variables["b"].append("a")
graph_of_variables["b"].append("d")
graph_of_variables["b"].append("e")
#or
graph_of_variables["a"] = ["b", "c", "d"]
graph_of_variables["b"] = ["a", "d", "e"]

if __name__ == "__main__":
    #run scripts here or in interactive mode
    pass

