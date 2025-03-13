import pandas as pd


def convert_to_category(df: pd.DataFrame, categorical_cols: list) -> pd.DataFrame:
    """
    Convert specified columns of a DataFrame to the categorical data type.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the accident data.
    categorical_cols : list
        List of column names to be converted to the category data type.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the specified columns converted to category type.

    Notes
    -----
    - Converting columns to category reduces memory usage and improves processing speed.
    - Ensure that the provided column names exist in the DataFrame before calling this function.
    - The function modifies the original DataFrame and returns the updated version.
    """
    df[categorical_cols] = df[categorical_cols].astype("category")
    return df


def display_unique_values(df: pd.DataFrame, columns_to_skip: list) -> None:
    """
    Display the unique values for each column in the DataFrame,
    excluding specified columns.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the dataset.
    columns_to_skip : list
        List of column names to be excluded from the unique values check.

    Returns
    -------
    None
        This function prints the unique values for each column,
        excluding the specified ones.

    Notes
    -----
    - The function iterates through all columns in the DataFrame.
    - Columns listed in `exclude_columns` are skipped.
    - Unique values for each remaining column are printed.
    """
    print("\nUnique Values per Column:")

    for column in df.columns:
        if column not in columns_to_skip:
            unique_values = df[column].unique()
            print(f"{column}: {len(unique_values)} unique values.")


def generate_severity_counts(
    df: pd.DataFrame, column_name: str = "Accident_Severity"
) -> pd.Series:
    """
    Calculates the percentage distribution of accident severity levels in the given DataFrame column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing accident data.
    column_name (str): The column name that contains the accident severity levels (default is "Accident_Severity").

    Returns:
    pd.Series: A Series containing the percentage distribution of each severity level.

    Example:
    >>> df = pd.DataFrame({'Accident_Severity': ['Slight', 'Serious', 'Fatal', 'Slight', 'Slight']})
    >>> generate_severity_distribution(df)
    Slight: 60.00 %
    Serious: 20.00 %
    Fatal: 20.00 %
    """

    # Calculate the percentage distribution of accident severity levels
    severity_distribution = df[column_name].value_counts(normalize=True) * 100

    return severity_distribution


def display_severity_counts(severity_counts: pd.Series) -> None:
    """
    Displays the severity distribution as percentages in a user-friendly format.

    Parameters:
    severity_counts (pd.Series): The Series containing the percentage distribution of accident severity.

    Example:
    >>> severity_counts = pd.Series({'Slight': 60.0, 'Serious': 20.0, 'Fatal': 20.0})
    >>> display_severity_counts(severity_counts)
    Slight: 60.00 %
    Serious: 20.00 %
    Fatal: 20.00 %
    """

    # Display the severity levels and their corresponding percentage values
    for severity, percentage in severity_counts.items():
        print(f"{severity}: {percentage:.2f} %")
