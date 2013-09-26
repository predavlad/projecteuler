def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    if not is_weekend and 40 <= cigars <= 60:
        return True
    return False

assert not cigar_party(30, False)
assert cigar_party(50, False)
assert cigar_party(70, True)