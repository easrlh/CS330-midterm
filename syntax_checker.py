import syntax_checker_lib as sc

def main():
    # read in the source
    f = open("BLevel.txt", "r")
    # Next, get all lines from the file:
    b_code = f.read()

    # call method to remove comments
    b_code = sc.remove_comments(b_code)

    # call method to remove imports
    b_code = sc.remove_imports(b_code)

    # call method to verify class is properly defined
    b_code = sc.verify_class_definition(b_code)

    # call method to verify method is properly defined
    b_code = sc.verify_method_syntax(b_code)

    b_code = sc.check_scanner(b_code)

    # call method to verify different statements are properly defined
    b_code = sc.verify_statements(b_code)

    # method to remove print methods
    b_code = sc.verify_print_methods(b_code)

    # method check while loop syntax
    b_code = sc.check_while_loop(b_code)

    # method to check if/else blocks
    b_code = sc.check_if_block(b_code)
    
    # method to grab the leftovers, the errors
    b_code = sc.grab_leftovers(b_code)

    f.close()

main()
