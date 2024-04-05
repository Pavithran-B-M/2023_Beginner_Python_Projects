import csv 
import tkinter
from tkinter.filedialog import askopenfilename
from collections import namedtuple

Task = namedtuple("Task", ["title", "duration", "prerequisites"])



def read_task(filename) : #this functions purpose is to process and analyze the data in the csv file and make it compatable

    tasks = {} #creates an empyt dictionary to and stored in a variable called tasks
    
    for row in csv.reader(open(filename)) :
        
        number = int(row[0])
        
        title = row[1] # the value inside the square brackets is the index number for each coloumn, index starts at 0

        duration = float(row[2])

        prerequisites = set(map(int, row[3].split())) #convert the value of to int 

# from line 13 to 18 the data in the csv file is stored in respective variables 

        tasks[number] = Task(title, duration, prerequisites) # the named tuple Task is stored in a dictionary called tasks (nametuple is a data set similar to dictionary with keys)

    return tasks #returns the dictionary of stored data

def order_tasks(tasks): # the following functions purpose is the order the tasks from the tasks dictionary

    incomplete = set(tasks) #defaults the add all tasks in this dictionary as incomplete

    completed = set() #no tasks start completed so it creats an empty set

    start_days = {} #empty dictionary with no start days computed 

# lin 29 - 33 is setting all the tasks to incomplete and begins with no start days
    while incomplete:

        for task_number in incomplete:

            task = tasks[task_number] # index through each task in incomplete tasks dictionary

            if task.prerequisites.issubset(completed):
                earliest_start_day = 0 #sets the earliest start day to 0 for the first tasks

                for prereq_number in task.prerequisites:
                    prereq_end_day = start_days[prereq_number] + tasks[prereq_number].duration #calculates the end day of a tasks by adding the duration of a prereq task to the startday

                    if prereq_end_day > earliest_start_day:

                        earliest_start_day = prereq_end_day  # 

                start_days[task_number] = earliest_start_day 
                incomplete.remove(task_number) #removes task from incomplete dictoinary 
                completed.add(task_number) #adds processed tasks in to the completed dictionrary 
                
                break 

    return start_days 

def draw_chart(tasks, canvas, row_height=40, title_width=300, line_height=40, day_width= 20, #the following function deals with creating the Gantt chart, from the base lines of the chart to the length of each bar
               bar_height= 20, title_indent= 20, font_size= -16) :
    height = canvas["height"] # retrieves the hieght from delared variable ~ canvas = 
    width = canvas["width"]

    week_width = 5 * day_width # assuming there are 5 days in the week
    canvas.create_line(0, row_height, width, line_height, fill="gray")

    for week_number in range(5) : # the variable week number is an list of integers from 0-4
        x = title_width + week_number * week_width # calculates the horizontal position of the vertical line of the current week
        canvas.create_line(x, 0, x, height, fill="gray") # draws a vertical line from top to bottom of canvas at the calculated horizontal x position 
        canvas.create_text(x + week_width / 2, row_height / 2, text=f"Week {week_number+1}", font=("Helvetica", font_size, "bold"))

        start_days = order_tasks(tasks)

        y = row_height #starts with y, one row down from the top of the canvas

        for task_number in start_days:

            task = tasks[task_number] # declares a variable called task and indexes through each task_number in the tasks dictonary

            canvas.create_text(title_indent, y + row_height / 2, text = task.title, anchor=tkinter.W, font=("Helvetica", font_size )) # creates the task title on the left of the chart/ the parameters set the font and coordinates of the title of each task

            bar_x = title_width + start_days[task_number] * day_width

            bar_y = y + (row_height - bar_height) / 2 

            bar_width = task.duration * day_width # takes the number of days to complete the task [duration] and multiplies by the width of one day
            
            canvas.create_rectangle (bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, fill = "red") #creates the bar of the Gantt chart using the x, y coordinates calculated from before

            y += row_height # sets new y by add y plus another row height ~ next task qued 

def clear_canvas(): # the following function is used to clear the canvas 

    #filename_label.config(text="")

    canvas.delete(tkinter.ALL)


def open_project(): #the following function serves to open a csv file when a button is pressed 

    filename = askopenfilename(title="Open Project", initialdir=".", filetypes=[("CSV Document", "*.csv")]) #askopenfile is a function to open the file explorer on this PC

    tasks = read_task("ProjectPlanner\project.csv") 

    draw_chart(tasks, canvas)

    filename_label.config(text=filename)



tasks = read_task("ProjectPlanner\project.csv") # when adding files in the bracket remeber to provide the relative path

root = tkinter.Tk() #creates a top-level window widget 
root.resizable(width=False, height= False) # prevents the canvas window height from being resized
root.title("Project-Planner") # give the window a title

button_frame = tkinter.Frame(root, padx=5, pady=5)
button_frame.pack(side="top", fill="x")

open_button = tkinter.Button(button_frame, text="Open project...,", command= open_project) # creates a formatted button
open_button.pack(side="left") # places the formated button in part of the root window

clear_button = tkinter.Button(button_frame, text="Clear", command=clear_canvas)
# line 127 and 129 are used to create the clear button and pack the button in a particular location, respectively
clear_button.pack(side="left")

filename_label = tkinter.Label(button_frame)
filename_label.pack(side="right")

canvas = tkinter.Canvas(root, width = 800, height = 400, bg ="white") # creates a canvas widget 
canvas.pack(side="bottom") #packs the canvas widget at the bottom

tkinter.mainloop()
