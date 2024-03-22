from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["pikachu", "squirtle", "charmander"])
table.add_column("Type", ["electric", "water", "fire"])

print(table)