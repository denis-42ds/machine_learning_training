import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    # Initialize the initial approximation of the eigenvector
    n = data.shape[0]
    eigenvector = np.random.rand(n)
    eigenvector /= np.linalg.norm(eigenvector)

    # Iterative process of the power method
    for _ in range(num_steps):
        # Multiply the matrix by the current eigenvector
        product = np.dot(data, eigenvector)
        # Normalize the resulting product
        eigenvector = product / np.linalg.norm(product)

    # Compute the eigenvalue
    eigenvalue = float(np.dot(np.dot(data, eigenvector), eigenvector))

    return eigenvalue, eigenvector