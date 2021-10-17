# This entrypoint file to be used in development. Start by reading README.md

# from pytest import main

from arithmetic_arranger import arithmetic_arranger

# How to make to consideration one or two arguments
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'], True))

# Run unit tests automatically
# main()
