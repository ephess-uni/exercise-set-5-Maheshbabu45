import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Complete the data processing steps using numpy here.
    data = np.loadtxt(INFILE, delimiter=',')
    data -= np.mean(data)
    data /= np.std(data)
    processed = data
    # Save the output to OUTFILE using numpy routines.
    np.savetxt(OUTFILE, processed, delimiter=',')
