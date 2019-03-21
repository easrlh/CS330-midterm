import re

# has to find incorrect syntax and flag it

# method to remove comments
def remove_comments(file):
    pattern1 = "//.+\n"
    pattern2 = "/\*([\s\S]*?)\*/"
    # delete one line comments
    file = re.sub(pattern1, "\n", file)
    # print(file)
    # delete multi-line comments
    file = re.sub(pattern2, "\n", file)
    # print(file)
    return file

# method to remove imports
def remove_imports(file):
    # the below commented code was an error checking idea I had to make sure imports came before class
    """pattern = "^import\s|^class\s"
    results = re.findall(pattern, file)
    print(results)
    stop = results.index("class")
    if len(results) > (stop + 1):
        i = stop
        while i < len(results):
            if results(i) != "class":
                print("Error! Please put all your imports at the top of the file!")
            i += 1
    """
    pattern2 = "import\s.+;"
    file = re.sub(pattern2, "\n", file)
    # print(file)
    return file

# method to verify class is properly defined
# and that nothing comes before class now (except maybe spaces and newlines) that import and comments are gone
def verify_class_definition(file):
    pattern = "^\s*\n*class\s[A-Z]\w*\s{|^\s*\n*class\s[A-Z]\w*{"
    if re.search(pattern, file):
        file = re.sub(pattern, "", file)
        # print(file)
        file = remove_whitespace(file)
        # check and remove ending curly brace, if main ends in if{} or else{} then must have an added note in if blocks method to make sure main and class end in }
        pattern2 = "}$"
        if re.search(pattern2, file):
            file = re.sub(pattern2, "", file)
        else:
            print("Please add closing curly brace to your class declaration!")
    else: 
        print("Make sure that your file has a class declaration and that the only code above the class declaration are comments or imports!")

    # print(file)
    return file

# method to remove whitespace and make file all one line
def remove_whitespace(file):
    pattern = "\s+|\n"
    file = re.sub(pattern, "", file)
    # print(file)
    return file

# method to verify method is properly defined
# if public is at start of line, good, if not then error
def verify_method_syntax(file):
    pattern = "^publicstaticvoidmain\(String\[\]args\){"
    if re.search(pattern, file):
        file = re.sub(pattern, "", file)
        # print(file)
        # check and remove ending curly brace
        pattern2 = "}$"
        if re.search(pattern2, file):
            file = re.sub(pattern2, "", file)
        else:
            print("Please add a closing curly brace to your main method!")
        # print(file)
    else:
        print("Make sure that your file has a main method and that it comes directly after your class declaration! There should be no code above class declaration and main method after removing comments and imports!")

    return file


# method for scanner creation
def check_scanner(file):
    pattern = "Scanner[a-z]\w*=newScanner\(System\.in\);"

    file = re.sub(pattern, "", file)

    return file

# method to verify assignment statements are properly defined
def verify_statements(file):
    # print(file)
    # verify LHS for int/String/boolean instantiations and variable statements
    pattern = "int[a-z]\w*=|String[a-z]\w*=|boolean[a-z]\w*=|[a-z]\w*="
    # search and return true if it's there
    if re.search(pattern, file):
        # verify RHS (all possible RHS)
        pattern2 = '[a-z]\w*\+\d+;|\d+;|"\w*";|false;|true;|"\w*"\+[a-z]\w*\+"\w*";|"\w*"\+[a-z]\w*;|[a-z]\w*\+"\w*";|[a-z]\w*\.next\(\);|[a-z]\w*\.nextInt\(\);'
        if re.search(pattern2, file):
            file = re.sub(pattern, "", file)
            # print(file)
            file = re.sub(pattern2, "", file)
            # print(file)
        else:
            print("Please add RHS to statements!")

    return file

def verify_print_methods(file):
    # print(file)

    pattern = 'System.out.println\("[^"]*"\);|System.out.println\("[^"]*"\+\w+\);'
    file = re.sub(pattern, "", file)

    # print(file)

    return file

# method to check while loops
def check_while_loop(file):
    # this pattern captures conditionals being compared to #s or other vars via ==, !=, <=, >=, <, and > as well as boolean (var) and (!var)
    pattern = 'while\([a-z]\w*\){}|while\(![a-z]\w*\){}|while\([a-z]\w*==\d+\){}|while\([a-z]\w*==[a-z]\w*\){}|while\([a-z]\w*!=\d+\){}|while\([a-z]\w*!=[a-z]\w*\){}|while\([a-z]\w*<\d+\){}|while\([a-z]\w*<[a-z]\w*\){}|while\([a-z]\w*>\d+\){}|while\([a-z]\w*>[a-z]\w*\){}|while\([a-z]\w*<=\d+\){}|while\([a-z]\w*<=[a-z]\w*\){}|while\([a-z]\w*>=\d+\){}|while\([a-z]\w*>=[a-z]\w*\){}'

    file = re.sub(pattern, "", file)
    
    # print(file)

    return file

def check_if_block(file):
    # checks for if{}else{} first to make sure no else{} is accidentally left standing on its own (because that would be read as an error)
    pattern1 = 'if\([a-z]\w*\){}else{}|if\(![a-z]\w*\){}else{}|if\([a-z]\w*==\d+\){}else{}|if\([a-z]\w*==[a-z]\w*\){}else{}|if\([a-z]\w*!=\d+\){}else{}|if\([a-z]\w*!=[a-z]\w*\){}else{}|if\([a-z]\w*<\d+\){}else{}|if\([a-z]\w*<[a-z]\w*\){}else{}|if\([a-z]\w*>\d+\){}else{}|if\([a-z]\w*>[a-z]\w*\){}else{}|if\([a-z]\w*<=\d+\){}else{}|if\([a-z]\w*<=[a-z]\w*\){}else{}|if\([a-z]\w*>=\d+\){}else{}|if\([a-z]\w*>=[a-z]\w*\){}else{}'
    if re.search(pattern1, file):
        file = re.sub(pattern1, "", file)
        # print(file)
        # checks for ifs without else
        pattern2 = 'if\([a-z]\w*\){}|if\(![a-z]\w*\){}|if\([a-z]\w*==\d+\){}|if\([a-z]\w*==[a-z]\w*\){}|if\([a-z]\w*!=\d+\){}|if\([a-z]\w*!=[a-z]\w*\){}|if\([a-z]\w*<\d+\){}|if\([a-z]\w*<[a-z]\w*\){}|if\([a-z]\w*>\d+\){}|if\([a-z]\w*>[a-z]\w*\){}|if\([a-z]\w*<=\d+\){}|if\([a-z]\w*<=[a-z]\w*\){}|if\([a-z]\w*>=\d+\){}|if\([a-z]\w*>=[a-z]\w*\){}'
        if re.search(pattern2, file):
            file = re.sub(pattern2, "", file)
            # print(file)
        else:
            print("Be sure that every opening brace has a closing braces! Disregard this message if there are no if{} blocks (without else{}) in your code.")
    else:
        print("Be sure that every opening brace has a closing braces! Disregard this message if there are no if{}else{} blocks in your code.")

    return file

# any leftovers not deleted by subs are errors! This is communicated to the programmer as feedback
def grab_leftovers(file):
    pattern = ".+"
    error = re.search(pattern, file)
    if error:
        print("You have errors in your code! Review around this code:")
        print(error.group())
    else:
        print("Besides the errors above, if any, your code is error free!")

