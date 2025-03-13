import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def export_figure(filename: str) -> None:
    """
    Saves the current figure as an image in the 'images' directory.

    Parameters
    ----------
    filename : str
        Name of the output image file.
    """
    output_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path, bbox_inches="tight")


def plot_severities_distribution(
    series: pd.Series, palette: str = "magma", save_img: bool = False
) -> None:
    """
    Plots a bar chart showing the percentage distribution of accident severities.

    Parameters
    ----------
    series : pd.Series
        A Pandas Series where the index represents severity levels
        and the values represent the percentage of accidents.
    palette : str, default "magma"
        The color palette used for the bars in the plot.
    save_img : bool, default False
        If True, saves the plot as an image file.

    Returns
    -------
    None
        Displays the plot.
    """

    # Creating the bar chart
    plt.figure(figsize=(16, 6))
    sns.barplot(
        x=series.index,
        y=series.values,
        hue=series.index,
        palette=palette,
        legend=False,  # Disables the legend since hue is only for color distinction
    )

    # Setting the title and axis labels
    plt.title("Percentage of Accidents by Severity", fontsize=14, fontweight="bold")
    plt.xlabel("Level of Severity", fontsize=14, labelpad=20)
    plt.ylabel("Percentage of Accidents (%)", fontsize=14, labelpad=20)

    # Formatting tick labels for better readability
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Saves the image if save_img is True
    if save_img:
        export_figure("Accidents_Severity.png")

    # Display the plot
    plt.show()


def plot_accidents_by_month(accident_counts: pd.Series, save_img: bool = False) -> None:
    """
    Plots a line chart showing the number of serious or fatal accidents per month.

    Parameters
    ----------
    accident_counts : pd.Series
        A pandas Series where the index represents the months and the values represent
        the number of serious or fatal accidents for each month.

    save_img : bool, optional, default: False
        If True, saves the plot as a PNG image in the current directory.

    Returns
    -------
    None
        Displays the plot and optionally saves it as a file.

    Notes
    -----
    The function uses Seaborn for styling and Matplotlib for plotting.
    """

    # Set Seaborn color palette for the plot
    sns.set_palette("bright")

    # Create a new figure for the line plot with a specific size
    plt.figure(figsize=(18, 6))

    # Plot the accident data as a line chart with markers
    sns.lineplot(
        x=accident_counts.index,
        y=accident_counts.values,
        marker="o",
        linestyle="-",
        legend=True,
    )

    # Customize the title and axis labels
    plt.title(
        "Number of Serious or Fatal Accidents by Month", fontsize=16, fontweight="bold"
    )
    plt.xlabel("Month", fontsize=14, labelpad=20)
    plt.ylabel("Number of Accidents", fontsize=14, labelpad=20)

    # Style the axis ticks and grid
    plt.xticks(rotation=45, ha="center", fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(visible=False)

    # Adjust layout to prevent clipping of labels
    plt.tight_layout()

    # Save the plot as an image if requested
    if save_img:
        export_figure("Serious_Accidents_By_Month.png")

    # Display the plot
    plt.show()


def plot_vehicle_types(
    list_of_counts: list, list_of_labels: list, df: pd.DataFrame, save_img: bool = False
) -> None:
    """
    Plots a bar chart displaying the number of accidents per vehicle type.

    Parameters
    ----------
    list_of_counts : list
        A list containing the counts of accidents corresponding to each vehicle type.

    list_of_labels : list
        A list of labels to differentiate the vehicle types (e.g., the categories or classes).

    df : pd.DataFrame
        A pandas DataFrame that contains the accident data, including a column for vehicle types.

    save_img : bool, optional, default: False
        If True, saves the plot as a PNG image in the 'images' directory.

    Returns
    -------
    None
        Displays the plot and optionally saves it as a file.

    Notes
    -----
    The function uses Seaborn for styling and Matplotlib for plotting.
    """

    # Create a bar chart with the specified size
    plt.figure(figsize=(20, 10))

    # Create the bar plot using Seaborn's barplot function
    sns.barplot(
        x=list_of_counts,
        y="count",
        data=df,
        palette="Dark2",
        hue=list_of_labels,
        legend=True,
    )

    # Set the title and axis labels
    plt.title("Number of Accidents per Vehicle Type", fontsize=20, fontweight="bold")
    plt.xlabel("Type of Vehicle", fontsize=18, fontweight="bold", labelpad=5)
    plt.ylabel("Number of Accidents", fontsize=18, fontweight="bold", labelpad=20)

    # Style the x-axis labels (vehicle types) and the y-axis ticks
    plt.xticks(
        ticks=range(len(df)),
        labels=df["Vehicle_Type"],
        rotation=45,
        ha="center",
        fontsize=14,
    )
    plt.yticks(fontsize=15)

    # Style the legend
    plt.legend(
        title="Vehicle Types",
        title_fontsize=16,
        fontsize=15,
        loc="upper left",
        borderpad=0.5,
        labelspacing=0.6,
        handlelength=1.5,
    )

    # Adjust the layout to avoid clipping of elements
    plt.tight_layout()

    # Save the figure if requested
    if save_img:
        plt.savefig("images/Vehicle_Types.png")

    # Display the plot
    plt.show()


def plot_other_conditions(dataframe: pd.DataFrame) -> None:
    """
    Plots bar charts displaying the percentage of accidents for each condition type in the dataframe.

    Parameters
    ----------
    dataframe : pd.DataFrame
        A pandas DataFrame where each column represents a condition type (road surface, weather, and light conditions)
        and contains categorical values representing different conditions.

    Returns
    -------
    None
        Displays the bar charts and saves them as PNG images in the 'images' directory.

    Notes
    -----
    The function generates a bar plot for each condition type, showing the percentage of accidents for each condition.
    The plots are saved in the current working directory under the 'images' folder.
    """

    # Initialize an accumulator for cycling through color palettes
    accumulator = 0
    palette_list = ["Dark2", "plasma", "magma"]

    # Loop through the dataframe columns to generate plots for each condition type
    for condition_type in dataframe:
        # Calculate the percentage of each value for the current condition type
        values_count = dataframe[condition_type].value_counts(normalize=True) * 100

        # Create a new figure for the bar plot
        plt.figure(figsize=(20, 8))

        # Generate the bar plot using Seaborn
        sns.barplot(
            x=values_count.index,
            y=values_count.values,
            hue=values_count.index,
            palette=palette_list[accumulator % len(palette_list)],
            legend=True,
        )

        # Set the title and labels for the plot
        plt.title(
            f"Percentage of Accidents per {condition_type.replace('_', ' ').title()}",
            fontsize=18,
            fontweight="bold",
        )
        plt.xlabel(
            f"{condition_type.replace('_', ' ').title()}",
            fontsize=16,
            fontweight="bold",
            labelpad=25,
        )
        plt.ylabel(
            "Percentage of Accidents", fontsize=16, fontweight="bold", labelpad=25
        )

        # Style the x and y axis labels
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        # Style the legend
        plt.legend(
            title=f"{condition_type.replace('_', ' ').title()}",
            title_fontsize=15,
            fontsize=15,
            borderpad=1.5,
            labelspacing=0.7,
        )

        # Increment the accumulator to cycle through palettes
        accumulator += 1

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Save the plot as an image in the 'images' directory
        output_dir = os.path.join(os.getcwd(), "images")
        os.makedirs(
            output_dir, exist_ok=True
        )  # Create the directory if it doesn't exist
        output_path = os.path.join(output_dir, f"{condition_type}.png")
        plt.savefig(output_path, bbox_inches="tight")

        # Display the plot
        plt.show()


def plot_junction_control(df: pd.DataFrame, save_img: bool = False) -> None:
    """
    Plots a bar chart displaying the number of accidents for each type of junction control.

    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame containing the data, with the column "Junction_Control" representing
        different types of junction control.

    save_img : bool, optional, default: False
        If True, saves the plot as an image file in the current directory.

    Returns:
    --------
    None
        This function does not return any value. It directly displays or saves the plot.

    Notes:
    ------
    - The function uses seaborn's `barplot` to generate a bar chart.
    - The plot shows the count of accidents per junction control type.
    """

    # Get the count of each unique value in the "Junction_Control" column
    junction_control_series = df["Junction_Control"].value_counts()

    # Create the plot with specified size
    plt.figure(figsize=(20, 8))

    # Create a barplot showing the count of accidents per junction control type
    sns.barplot(
        x=junction_control_series.index,
        y=junction_control_series.values,
        hue=junction_control_series.index,
        palette="magma",
        legend=True,
    )

    # Set the title and axis labels with appropriate font sizes
    plt.title("Junction Control Types", fontsize=18, fontweight="bold")
    plt.xlabel("Junction Control Type", fontsize=16, fontweight="bold", labelpad=25)
    plt.ylabel("Number of Accidents", fontsize=16, fontweight="bold", labelpad=25)

    # Style the legend with font size and label spacing
    plt.legend(
        title="Junction Control", title_fontsize=15, fontsize=15, labelspacing=0.6
    )

    # Set the font size for x and y ticks
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Ensure tight layout to avoid overlapping elements
    plt.tight_layout()

    # Save the plot as an image if requested
    if save_img:
        export_figure("Junction_Control_Types.png")

    # Display the plot
    plt.show()
