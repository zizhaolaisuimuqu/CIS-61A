def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    attempts = 0
    attempts_pwd = []
    def box(amount, input_pwd):
        nonlocal balance, password, attempts, attempts_pwd
        if attempts >= 3:
            return f'Your account is locked. Attempts: {attempts_pwd}'
        elif password != input_pwd:
            attempts_pwd.append(input_pwd)
            attempts += 1
            return 'Incorrect password'
        elif amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return box