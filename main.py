from typing import List, Dict, Tuple

file_path = "C:/Users/HP/Desktop/Fast Track/Data.txt"

def load_data_as_dict(file_path: str) -> Dict[str, List[str]]:
    """
    Reads a text file and converts it into a dictionary.
    Each key is a column name, and each value is a list of entries in that column.
    """
    data: Dict[str, List[str]] = {}
    current_column: str | None = None  # Holds the current column name

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line == "END":
                break

            if line.startswith("COLUMN"):
                current_column = line[7:].strip()
                data[current_column] = []
            elif current_column:
                data[current_column].append(line)

    return data

def load_data_as_list(file_path: str) -> List[Tuple[str, List[str]]]:
    """
    Reads the file and converts it into a list of tuples.
    Each tuple has the column name and a list of entries.
    """
    data: List[Tuple[str, List[str]]] = []
    current_column: str | None = None
    current_list: List[str] = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line == "END":
                break

            if line.startswith("COLUMN"):
                if current_column is not None:
                    data.append((current_column, current_list))
                current_column = line[7:].strip()
                current_list = []
            elif current_column:
                current_list.append(line)

        if current_column is not None:
            data.append((current_column, current_list))

    return data


def return_sublist(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> List[str] | None:
    """
    Returns the list of values under the given column name.
    Works with either a dictionary or a list of tuples.
    Returns None if the column doesn't exist or the data type is invalid.
    """
    if isinstance(data, dict):
        return data.get(col_name)

    elif isinstance(data, list):
        for col, values in data:
            if col == col_name:
                return values

    return None


def return_sublist_total(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> float | None:
    """
    Returns the total (sum) of all numeric values under the given column.
    Returns None if any value can't be converted to float.
    """
    values: List[str] | None = return_sublist(data, col_name)

    if values is None:
        return None

    try:
        total: float = sum(float(value) for value in values)
        return total
    except ValueError:
        return None


def return_sublist_mean(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> float | None:
    """
    Returns the average (mean) of numeric values under the given column.
    Returns None if any value can't be converted to float.
    """
    values: List[str] | None = return_sublist(data, col_name)

    if values is None:
        return None

    try:
        float_values: List[float] = [float(value) for value in values]
        return sum(float_values) / len(float_values)
    except ValueError:
        return None


# from typing import List, Dict, Tuple, Any
# #file_path = "C:/Users/HP/Desktop/Fast Track/Data.txt"
#
# def load_data_as_dict(file_path: str) -> Dict[str, List[str]]:
#     """
#     Reads a text file and converts it into a dictionary.
#     Each key is a column name, and each value is a list of entries in that column.
#     """
#     data: Dict[str, List[str]] = {}
#     current_column: str | None = None  # Holds the current column name
#
#     with open(file_path, "r") as file:
#         for line in file:
#             line = line.strip()
#
#             if line == "END":
#                 break
#
#             if line.startswith("COLUMN"):
#                 current_column = line[7:].strip()
#                 data[current_column] = []
#             elif current_column:
#                 data[current_column].append(line)
#
#     return data
#
#
# def load_data_as_list(file_path: str) -> List[Tuple[str, List[str]]]:
#     """
#     Reads the file and converts it into a list of tuples.
#     Each tuple has the column name and a list of entries.
#     """
#     data: List[Tuple[str, List[str]]] = []
#     current_column: str | None = None
#     current_list: List[str] = []
#
#     with open(file_path, "r") as file:
#         for line in file:
#             line = line.strip()
#
#             if line == "END":
#                 break
#
#             if line.startswith("COLUMN"):
#                 if current_column is not None:
#                     data.append((current_column, current_list))
#                 current_column = line[7:].strip()
#                 current_list = []
#             elif current_column:
#                 current_list.append(line)
#
#         if current_column is not None:
#             data.append((current_column, current_list))
#
#     return data
#
#
# def return_sublist(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> List[str] | None:
#     """
#     Returns the list of values under the given column name.
#     Works with either a dictionary or a list of tuples.
#     Returns None if the column doesn't exist or the data type is invalid.
#     """
#     if isinstance(data, dict):
#         return data.get(col_name)
#
#
#     elif isinstance(data, list):
#         for col, values in data:
#             if col == col_name:
#                 return values
#
#     return None
#
#
# def return_sublist_total(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> float | None:
#     """
#     Returns the total (sum) of all numeric values under the given column.
#     Returns None if any value can't be converted to float.
#     """
#     values: List[str] | None = return_sublist(data, col_name)
#
#     if values is None:
#         return None
#
#     try:
#         total: float = sum(float(value) for value in values)
#         return total
#     except ValueError:
#         return None
#
#
# def return_sublist_mean(data: Dict[str, List[str]] | List[Tuple[str, List[str]]], col_name: str) -> float | None:
#     """
#     Returns the average (mean) of numeric values under the given column.
#     Returns None if any value can't be converted to float.
#     """
#     values: List[str] | None = return_sublist(data, col_name)
#
#     if values is None:
#         return None
#
#     try:
#         float_values: List[float] = [float(value) for value in values]
#         return sum(float_values) / len(float_values)
#     except ValueError:
#         return None
#
# # Your function definitions should be here first...
# # Example:
# # def load_data_as_dict(file_path: str) -> dict[str, list[str | int]]:
# #     ...
#
# def main() -> None:
#     # Define your file path
#     file_path: str = "data.txt"
#
#     # Load data as a dictionary
#     dict_data = load_data_as_dict(file_path)
#     print("Data as dictionary:")
#     print(dict_data)
#     print()
#
#     # Load data as a list of tuples
#     list_data = load_data_as_list(file_path)
#     print("Data as list of tuples:")
#     print(list_data)
#     print()
#
#     # Choose a column name to work with (must match what's in data.txt)
#     column_name: str = "Names"  # Replace with an actual column from your file
#
#     # Get sublist from dictionary
#     sublist1 = return_sublist(dict_data, column_name)
#     print(f"Sublist from dictionary for column '{column_name}': {sublist1}")
#     print()
#
#     # Get sublist from list of tuples
#     sublist2 = return_sublist(list_data, column_name)
#     print(f"Sublist from list of tuples for column '{column_name}': {sublist2}")
#     print()
#
#     # Get total from the column
#     total = return_sublist_total(dict_data, column_name)
#     print(f"Total of column '{column_name}': {total}")
#     print()
#
#     # Get mean from the column
#     mean = return_sublist_mean(dict_data, column_name)
#     print(f"Mean of column '{column_name}': {mean}")
#     print()
#
# # Run the program
# if __name__ == "__main__":
#     main()
