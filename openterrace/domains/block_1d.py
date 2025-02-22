import numpy as np

def validate_input(vars, domain_shape):
    """Validates input arguments.

    Args:
        vars (list): List of arguments
        domain_shape (str): Name of domain type
    """
        
    required = ['n','A','L']
    for var in required:
        if not var in vars:
            raise Exception("Keyword \'"+var+"\' not specified for domain of type \'"+domain_shape+"\'")

def shape(vars):
    """Shape function.

    Args:
        vars (list): List of arguments
    """
    
    n = vars['n']
    return np.array([n])

def dx(vars):
    """Node spacing function.

    Args:
        vars (list): List of arguments
    """

    n = vars['n']
    L = vars['L']
    dx = L/(n-1)
    return np.repeat(dx, n)

def node_pos(vars):
    """Node position function.

    Args:
        vars (list): List of arguments
    """

    n = vars['n']
    L = vars['L']
    return np.array(np.linspace(0,L,n))

def A(vars):
    """Cross-sectional area for faces of node.

    Args:
        vars (list): List of arguments
    """

    n = vars['n']
    A = vars['A']
    return (np.repeat(A,n), np.repeat(A,n))

def V(vars):
    """Volume of node element.

    Args:
        vars (list): List of arguments
    """

    n = vars['n']
    A = vars['A']
    L = vars['L']
    dx = L/(n-1)
    face_pos_vec = np.concatenate(([0], np.linspace(dx/2,L-dx/2,n-1), [L]))
    return np.diff(A*face_pos_vec)