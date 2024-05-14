def unify(s, t, subs):
    if s == t:
        return subs
    elif isinstance(s, str) and s.islower() and s.isalpha():
        return unify_var(s, t, subs)
    elif isinstance(t, str) and t.islower() and t.isalpha():
        return unify_var(t, s, subs)
    elif isinstance(s, tuple) and isinstance(t, tuple) and len(s) == len(t):
        return unify(s[1:], t[1:], unify(s[0], t[0], subs))
    else:
        return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        subs[var] = x
        return subs

def main():
    s_input = input("Enter the first term (as a tuple): ")
    t_input = input("Enter the second term (as a tuple): ")
    s = eval(s_input)  # Evaluate user input to convert it to a tuple
    t = eval(t_input)  # Evaluate user input to convert it to a tuple
    subs = {}

    result = unify(s, t, subs)

    if result is None:
        print("Unification not possible.")
    else:
        print("Substitution:")
        for key, value in result.items():
            print(f"{key} = {value}")

if _name_ == "_main_":
    main()
