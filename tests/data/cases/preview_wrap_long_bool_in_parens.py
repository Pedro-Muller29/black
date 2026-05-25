# flags: --preview --line-length=88

# Regression test for https://github.com/psf/black/issues/2156.
# When a long line contains a single top-level `and`/`or`, splitting inside
# one of the operands' call arguments is uglier than wrapping the whole
# expression in optional parens. Black wraps in that case under --preview.

if not is_node_in_type_annotation_context(node) and isinstance(node.parent, astroid.Subscript):
    pass


def _supports_mapping_protocol(value: astroid.node_classes.NodeNG) -> bool:
    return _supports_protocol_method(value, GETITEM_METHOD) and _supports_protocol_method(value, KEYS_METHOD)


def deep():
    def deeper():
        def deepest():
            if getattr(func, "name", None) == "iterate" and utils.is_builtin_object(func):
                pass


# Assignment with a long boolean RHS still gets the wrap.
result = _supports_protocol_method(value, GETITEM_METHOD) and _supports_protocol_method(value, KEYS_METHOD)


# A single boolean with a set literal on the RHS keeps the inline split,
# since the set will naturally expand and wrapping just adds an indent level.
if grandparent is not None and grandparent.type in {syms.comp_for, syms.old_comp_for, syms.for_stmt}:
    return 0


# Multiple booleans already wrap via the existing `> 1` path; behavior is
# unchanged from stable.
return (
    is_postponed_evaluation_enabled(node)
    and value.qname() in SUBSCRIPTABLE_CLASSES_PEP585
    and is_node_in_type_annotation_context(node)
)


# `or` gets the same treatment as `and`.
if not is_node_in_type_annotation_context(node) or isinstance(node.parent, astroid.Subscript):
    pass


# `assert` and other statement contexts wrap the same way.
assert _supports_protocol_method(value, GETITEM_METHOD) and _supports_protocol_method(value, KEYS_METHOD)


# Short boolean expressions stay on one line.
if foo and bar(x):
    pass

# output

# Regression test for https://github.com/psf/black/issues/2156.
# When a long line contains a single top-level `and`/`or`, splitting inside
# one of the operands' call arguments is uglier than wrapping the whole
# expression in optional parens. Black wraps in that case under --preview.

if (
    not is_node_in_type_annotation_context(node)
    and isinstance(node.parent, astroid.Subscript)
):
    pass


def _supports_mapping_protocol(value: astroid.node_classes.NodeNG) -> bool:
    return (
        _supports_protocol_method(value, GETITEM_METHOD)
        and _supports_protocol_method(value, KEYS_METHOD)
    )


def deep():
    def deeper():
        def deepest():
            if (
                getattr(func, "name", None) == "iterate"
                and utils.is_builtin_object(func)
            ):
                pass


# Assignment with a long boolean RHS still gets the wrap.
result = (
    _supports_protocol_method(value, GETITEM_METHOD)
    and _supports_protocol_method(value, KEYS_METHOD)
)


# A single boolean with a set literal on the RHS keeps the inline split,
# since the set will naturally expand and wrapping just adds an indent level.
if grandparent is not None and grandparent.type in {
    syms.comp_for,
    syms.old_comp_for,
    syms.for_stmt,
}:
    return 0


# Multiple booleans already wrap via the existing `> 1` path; behavior is
# unchanged from stable.
return (
    is_postponed_evaluation_enabled(node)
    and value.qname() in SUBSCRIPTABLE_CLASSES_PEP585
    and is_node_in_type_annotation_context(node)
)


# `or` gets the same treatment as `and`.
if (
    not is_node_in_type_annotation_context(node)
    or isinstance(node.parent, astroid.Subscript)
):
    pass


# `assert` and other statement contexts wrap the same way.
assert (
    _supports_protocol_method(value, GETITEM_METHOD)
    and _supports_protocol_method(value, KEYS_METHOD)
)


# Short boolean expressions stay on one line.
if foo and bar(x):
    pass
