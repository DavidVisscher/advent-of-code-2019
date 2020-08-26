"""
Advent of code day 1

Rocket fuel calculator.
"""

total_fuel = 0

with open('modules.txt', 'r') as modulefile:
    for line in modulefile:
        moduleweight = int(line)
        print(f"M: {moduleweight}")
        module_fuel = (moduleweight // 3) -2
        total_fuel += module_fuel
        
        print(f"F: {module_fuel}")
        extra_fuel = module_fuel
        while extra_fuel > 0:
            extra_fuel = max((extra_fuel //3) -2, 0)
            print(f"    E: {extra_fuel}")
            total_fuel += extra_fuel

print(total_fuel)
