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

        print(f"Added task with id {new_id}")

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

        print(f"Updated  #{current_task['id']
                           } description to '{Main.args[3]}'")

    # delete task
    def delete_task(pos):
        pass

    # mark a task a todo
    def mark_task_todo(pos):
        pass

    # mark a task as in progress
    def mark_task_inprogress(pos):
        pass

    # mark a task as done
    def mark_task_done(pos):
        pass

    # list tasks
    def list_tasks():
        pass
        # list all
        # list by todo
        # list by done
        # list by in progress

    # get the task list and load it into a dict
    def load_json():
        with open(Main.path + "tasks-cli.json", "r") as file:
            Main.tasks = json.loads(file.readline())

    # store task list dict into json file
    def save_json():
        with open(Main.path + "tasks-cli.json", "w") as file:
            file.writelines(json.dumps(Main.tasks))

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

        # process args
        if len(Main.args) > 1:
            match Main.args[1]:
                case "add":
                    if len(Main.args) > 2:
                        Main.add_task(Main.args[2])
                    else:
                        print("Error: Description needed with 'add' argument")
                case "update":
                    if len(Main.args) > 2:
                        if len(Main.args) > 3:
                            try:
                                index = Main.find_by_id(Main.args[2])
                                Main.update_task(index)
                            except Exception as e:
                                print(
                                    f"ERROR: please provide valid integer for id\n {e}")
                        else:
                            print("ERROR: please provide valid integer for id")
                    else:
                        print("ERROR: please provide the id of the task to update.")
                case _:
                    print("ERROR: unknown error occured, likely no flags received")

        # save the file
        Main.save_json()
