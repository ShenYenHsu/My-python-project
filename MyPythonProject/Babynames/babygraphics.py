"""
File: babygraphics.py
Name: Shane
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # Calculate the width of line between line
    line_gap = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    initial_x = GRAPH_MARGIN_SIZE                   # The initial x position
    x_coordinate = initial_x+line_gap*year_index    # x position according to the year in YEARS list
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw the frame of the figure
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    # Draw vertical lines associated with the current year.
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Loop over the list of lookup_names
    color_index = 0
    for name in lookup_names:
        if name in name_data:
            year1 = str(YEARS[0])
            # Initial (x, y)
            x1 = get_x_coordinate(CANVAS_WIDTH, 0)
            # Check if rank is within 1000
            if year1 in name_data[name]:                                  # 補充說明:將20到580之間分成1000等分，每一等分為0.56
                y1 = int(name_data[name][year1])*0.56+GRAPH_MARGIN_SIZE   # *0.56 to make the rank number within frame
            else:
                y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            year_index = 0
            # Loop over the YEARS list to make a line
            for y in YEARS:
                x2 = get_x_coordinate(CANVAS_WIDTH, year_index)
                if str(y) in name_data[name]:                                   # Check if rank is within 1000
                    y2 = int(name_data[name][str(y)])*0.56+GRAPH_MARGIN_SIZE    # Rank number
                    # Create text
                    canvas.create_text(x2+TEXT_DX, y2, text=(name, name_data[name][str(y)]),
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                else:
                    y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(x2 + TEXT_DX, y2, text=(name, '*'),
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                # Create line
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])
                # Set for the next point
                x1 = x2
                y1 = y2
                year_index += 1
        # Set for the next name(line)
        color_index += 1
        if color_index == 4:    # The lookup_name list is more than 4 so the line color needs to be duplicated
            color_index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
