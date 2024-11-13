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

    # current time string
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")

    # add a task to the task list
    def add_task(desc):
        # figure out what the id for the new task will be.
        # we do it this way so that we don't end up with
        # two tasks with the same id after we delete a task
        new_id = (Main.tasks[Main.tasks.length - 1]["id"]) + 1

        # generate new task
        Main.tasks.append({
            "id": new_id,
            "description": desc,
            "status": "todo",
            "createdAt": Main.current_time,
            "updatedAt": Main.current_time,
        })

    # update task description
    def update_task(task_id):
        Main.tasks[task_id]["description"] = Main.args[3]

    # delete task
    def delete_task(task_id):
        pass

    # mark a task a todo
    def mark_task_todo(task_id):
        pass

    # mark a task as in progress
    def mark_task_inprogress(task_id):
        pass

    # mark a task as done
    def mark_task_done(task_id):
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
            Main.tasks = json.loads(file.readline)

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

        # save the file
        Main.save_json()
