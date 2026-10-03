import string
import secrets

AMBIGUOUS_CHARS = set("0O1lI|")


class InvalidPasswordOptionsError(Exception):
    pass


def _character_pools(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous):
    pools = {}
    if use_upper:
        pools["upper"] = string.ascii_uppercase
    if use_lower:
        pools["lower"] = string.ascii_lowercase
    if use_digits:
        pools["digits"] = string.digits
    if use_symbols:
        pools["symbols"] = "!@#$%^&*()-_=+[]{};:,.<>?"

    if exclude_ambiguous:
        pools = {name: "".join(c for c in chars if c not in AMBIGUOUS_CHARS)
                  for name, chars in pools.items()}

    return pools


def generate_password(length: int, use_upper: bool, use_lower: bool,
                       use_digits: bool, use_symbols: bool,
                       exclude_ambiguous: bool = False) -> str:
    """Generate a cryptographically secure password guaranteed to contain
    at least one character from every selected character type."""
    if length < 8:
        raise InvalidPasswordOptionsError("Password length must be at least 8 characters.")

    selected_count = sum([use_upper, use_lower, use_digits, use_symbols])
    if selected_count < 2:
        raise InvalidPasswordOptionsError("Select at least 2 character types.")

    pools = _character_pools(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous)
    pools = {name: chars for name, chars in pools.items() if chars}  # drop empty pools

    if len(pools) < 2:
        raise InvalidPasswordOptionsError(
            "Not enough usable characters left after excluding ambiguous characters. "
            "Select more character types or turn off ambiguous-character exclusion."
        )

    if length < len(pools):
        raise InvalidPasswordOptionsError(
            f"Password length must be at least {len(pools)} to include one of each selected type."
        )

    # Guarantee at least one character from every selected pool.
    required_chars = [secrets.choice(chars) for chars in pools.values()]

    all_chars = "".join(pools.values())
    remaining_length = length - len(required_chars)
    remaining_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    password_chars = required_chars + remaining_chars
    # Shuffle securely so the guaranteed characters aren't always at the front.
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def password_strength(password: str, type_count: int) -> str:
    """Classify strength as Weak / Medium / Strong based on length and
    character-type diversity (not the exact composition, to avoid leaking
    info about the password itself beyond what's already visible)."""
    length = len(password)
    if length >= 14 and type_count >= 3:
        return "Strong"
    elif length >= 10 and type_count >= 2:
        return "Medium"
    else:
        return "Weak"