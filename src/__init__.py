import sys
import json
import os
import datetime


class Main:
    # define path
    home_path = os.path.expanduser("~")
    path = home_path + "/.cache/tasks-cli/"

    # grab args
    args = sys.argv

    # list for tasks
    tasks = []

    # capture current time in a string
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")

    # add a task to the task list
    def add_task(desc):
        # figure out what the id for the new task will be.
        # we do it this way so that we don't end up with
        # two tasks with the same id after we delete a task
        new_id = (Main.tasks[len(Main.tasks) - 1]["id"]) + 1

        # generate new task
        Main.tasks.append({
            "id": new_id,
            "description": desc,
            "status": "todo",
            "createdAt": Main.current_time,
            "updatedAt": Main.current_time,
        })

        print(f"Added task with id [{new_id}]")

    # find a task by its id
    # returns NoneType if none is found
    def find_by_id(task_id):
        for x, task in enumerate(Main.tasks):
            if int(task['id']) == int(task_id):
                return x

    # update task description
    def update_task(pos):
        # task we are changing
        current_task = Main.tasks[pos]

        # change the description
        current_task["description"] = Main.args[3]

        # change the update time
        current_task["updatedAt"] = Main.current_time

        print(f"Updated task: id [{current_task['id']}] description to '{
              Main.args[3]}'")

    # delete task
    def delete_task(pos):
        Main.tasks.pop(pos)
        print(f"Successfully deleted task id [{Main.args[2]}]")

    # mark a task a todo
    def mark_task_in_progress(pos):
        Main.tasks[pos]['status'] = "in-progress"
        print(f"Updated task: id [{Main.args[2]}] status to 'in-progress'")

    # mark a task as done
    def mark_task_done(pos):
        Main.tasks[pos]['status'] = "done"
        print(f"Updated task: id [{Main.args[2]}] status to 'done'")

    # list tasks
    def list_tasks(option):
        count = 0
        message = ""

        for task in Main.tasks:
            if task['status'] == option or option == 'all':
                count += 1
                message += f"id [{task['id']}] '{task['description']}' \n    Status: {task['status']}\n    Created on:\t{
                    task['createdAt']}\n    Updated on:\t{task['updatedAt']}\n\n"
        if option == "all":
            print(f"Here's all {count} tasks:\n")
        else:
            print(f"Here's all {count} '{option}' tasks:\n")
        print(message)

    # get the task list and load it into a dict
    def load_json():
        with open(Main.path + "tasks-cli.json", "r") as file:
            Main.tasks = json.loads(file.readline())

    # store task list dict into json file
    def save_json():
        with open(Main.path + "tasks-cli.json", "w") as file:
            file.writelines(json.dumps(Main.tasks))

    def display_help():
        print("""
A simple and minimalistic CLI tool to track tasks!

usage: tasks-cli [option] [id | descr | status] [descr]

Options:
add (descr)             : Takes a (descr)iption of the task as a string.
update (id) (descr)     : Takes a task (id) as an integer, then a task (descr)iption as a string.
list [status]           : Takes an optional string for the status, defaults to showing all tasks.
                          Status can be one of the following: todo, done, or in-progress.
delete (id)             : Takes a task (id) as an integer and removes it completely from the task list.
help                    : Displays this message.
mark-in-progress (id)   : Changes status of given task by (id) to 'in-progress'
mark-done (id)          : Changes status of given task by (id) to 'done'

Detailed man page coming soon.
        """)

    # process args
    # this is a mess
    # remember: the first arg in args is the
    # file that is being called, so we ignore it
    def handle_args():
        # skip this function if there are no args
        if not len(Main.args) > 1:
            Main.display_help()
            return

        match Main.args[1]:
            case "add":
                if len(Main.args) > 2:
                    Main.add_task(Main.args[2])
                else:
                    print("Error: Description needed with 'add' argument")
            case "update":
                try:
                    index = Main.find_by_id(Main.args[2])
                except Exception as e:
                    print(f"ERROR: please provide valid id integer\n {e}")
                else:
                    Main.update_task(index)
            case "list":
                if len(Main.args) > 2:
                    Main.list_tasks(Main.args[2])
                else:
                    Main.list_tasks("all")
            case "help":
                Main.display_help()
            case "delete":
                if len(Main.args) > 2 and Main.args[2].isnumeric():
                    print(
                        f"Are you sure you want to delete task id [{Main.args[2]}]")
                    user_input = input("(y)es/(n)o: ")
                    if user_input.upper() == "Y" or user_input.upper() == "YES":
                        try:
                            pos = Main.find_by_id(int(Main.args[2]))
                            Main.delete_task(pos)
                        except Exception as e:
                            print(
                                f"ERROR: please provide a valid id integer\n {e}")
                    else:
                        return
                else:
                    print("ERROR: 'delete' requires valid task id")
            case "mark-in-progress":
                try:
                    pos = Main.find_by_id(int(Main.args[2]))
                    Main.mark_task_in_progress(pos)
                except Exception as e:
                    print(
                        f"ERROR: please provide a valid id integer\n {e}")
            case "mark-done":
                try:
                    pos = Main.find_by_id(int(Main.args[2]))
                    Main.mark_task_done(pos)
                except Exception as e:
                    print(f"ERROR: please provide a valid id integer\n {e}")
            case _:
                print("ERROR: unknown error occured, no flags received" +
                      "\nor incorrect flags received.")

    # main entry point
    def main():
        # Create the directory for the json file
        if not os.path.exists(Main.path):
            try:
                os.makedirs(Main.path)
            except FileExistsError:
                print(f"Directory '{Main.path}' already exists.")
            except PermissionError:
                print(f"Permission denied: Unable to create '{Main.path}'.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Load the json file
        Main.load_json()

        # handle the args
        Main.handle_args()

        # save the file
        Main.save_json()
