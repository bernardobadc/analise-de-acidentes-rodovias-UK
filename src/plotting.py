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


def plotting_severities_distribution(
    series: pd.Series, palette: str = "bright", save_img: bool = False
) -> None:
    # Creating the barchart
    plt.figure(figsize=(16, 6))
    sns.barplot(
        x=series.index,
        y=series.values,
        hue=series.index,
        palette=palette,
        legend=False,
    )

    # Setting the title and labels
    plt.title("Percentage of Accidents by Severity", fontsize=14, fontweight="bold")
    plt.xlabel("Level of Severity", fontsize=14, labelpad=20)
    plt.ylabel("Percentage of Accidents %", fontsize=14, labelpad=20)

    # Setting the ticks styles
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    if save_img == True:
        export_figure("Accidents_Severity.png")

    # Showing the plot
    plt.show()
