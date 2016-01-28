from decimal import Decimal

__author__ = 'yury_gnutov'


def nested_dict_diff(first, second, ignored=[]):
    """ Return a dict of keys that differ with another config object.
        If a value is not found in one fo the configs, it will be
        represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dictionary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    if first is None or second is None:
        assert False, "Nothing to compare"
    diff = {}
    sd1 = set(first)
    sd2 = set(second)
    ignored = set(ignored)
    # Keys missing in the second dict
    for key in sd1.difference(sd2).difference(ignored):
        diff[key] = 'key not found in second dict'
    # Keys missing in the first dict
    for key in sd2.difference(sd1).difference(ignored):
        diff[key] = 'key not found in first dict'
    # Check for differences
    for key in sd1.intersection(sd2).difference(ignored):
        second_val = second[key]
        first_val = first[key]
        if isinstance(second_val, (Decimal, long)):
            first_val = float(first_val)
            second_val = float(second_val)

        if isinstance(first_val, dict) or isinstance(second_val, dict):
            diff.update(nested_dict_diff(first_val, second_val, list(ignored)))
        elif isinstance(first_val, list) or isinstance(second_val, list):
            for fk, fv in zip(first_val, second_val):
                if isinstance(fk, dict) or isinstance(fv, dict):
                    diff.update(nested_dict_diff(fk, fv, ignored))
        else:
            if unicode(first_val) != unicode(second_val):
                diff[key] = (first_val, second_val)
    return diff
