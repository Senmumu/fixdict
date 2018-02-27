def fix_dict(data, ignore_duplicate_key=True, force=True):
    """
    Removes dots "." from keys, as mongo doesn't like that.
    If the key is already there without the dot, the dot-value get's lost.
    This modifies the existing dict!

    :param ignore_duplicate_key: True: if the replacement key is already in the dict, now the dot-key value will be ignored.
                                 False: raise ValueError in that case.
    """
    if isinstance(data, (list, tuple)):
        list2 = list()
        for e in data:
            list2.append(fix_dict(e))
        # end if
        return list2
    if isinstance(data, dict):
        # end if
        for key, value in data.items():
            value = fix_dict(value)
            old_key = key
            if "." in key:
                key = old_key.replace(".", "_")
                if key not in data:
                    data[key] = value
                else:
                    error_msg = "Dict key {key} containing a \".\" was ignored, as {replacement} already exists".format(
                        key=old_key, replacement=key)
                    if force:
                        import warnings
                        warnings.warn(error_msg, category=RuntimeWarning)
                    else:
                        raise ValueError(error_msg)
                    # end if
                # end if
                del data[old_key]
            if isinstance(value, int) and len(str(value)) > 8:
                value = str(value)
            # end if
            data[key] = value
        # end for
        return data
    # end if
    return data
# end def
