# logic/proofs.py

def direct_proof(statement, assumption, conclusion):
    """
    Improved direct proof:
    Check if a statement implies the conclusion, given the assumption.
    The function looks for common structures like "if assumption then conclusion".
    """
    # Simplify the statement, assumption, and conclusion to lowercase to avoid case-sensitivity issues
    statement = statement.lower()
    assumption = assumption.lower()
    conclusion = conclusion.lower()

    # Check if the statement contains an implication in the form "if assumption then conclusion"
    if "if" in statement and "then" in statement:
        parts = statement.split("then")
        if len(parts) == 2:
            if assumption in parts[0] and conclusion in parts[1]:
                return True

    return False


def contraposition_proof(statement, assumption, conclusion):
    """
    Proof by contraposition: prove if not conclusion implies not assumption.
    """
    # Negate assumption and conclusion for contraposition
    neg_assumption = "not " + assumption
    neg_conclusion = "not " + conclusion
    
    statement = statement.lower()
    assumption = assumption.lower()
    conclusion = conclusion.lower()

    if "if" in statement and "then" in statement:
        parts = statement.split("then")
        if len(parts) == 2:
            if neg_conclusion in parts[0] and neg_assumption in parts[1]:
                return True

    return False


def contradiction_proof(statement, assumption, contradiction):
    """
    Proof by contradiction: derive a contradiction from the assumption.
    """
    statement = statement.lower()
    assumption = assumption.lower()
    contradiction = contradiction.lower()

    # Check if assumption and statement lead to a contradiction
    return assumption in statement and contradiction in statement
