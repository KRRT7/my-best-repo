import ast


def ellipsis_in_ast_not_types(module: ast.AST) -> bool:
    def has_ellipsis_outside_types(node):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.Constant) and child.value is Ellipsis:
                # Check if the ellipsis is part of a type annotation
                if not isinstance(node, (ast.Subscript, ast.Index, ast.Tuple)):
                    return True
            if has_ellipsis_outside_types(child):
                return True
        return False
    
    return has_ellipsis_outside_types(module)
