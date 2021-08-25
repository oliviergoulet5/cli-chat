import sys

def query_yes_no(question, default = "yes"):
    valid = { "yes": True, "y": True, "no": False, "n": False }

    if default is None:
        prompt = "(y/n)"
    elif default is "yes":
        prompt = "(Y/n)"
    elif default is "no":
        prompt = "(y/N)"
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()

        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'.\n")