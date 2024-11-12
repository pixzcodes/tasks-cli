import sys
import json
import os


class Main:
    # define path
    home_path = os.path.expanduser("~")
    path = home_path + "/.cache/tasks-cli/"

    # grab args
    args = sys.argv

    # for testing purposes
    tasks = {
        1: "Shop groceries",
        2: "Take out the trash",
        3: "Wash dishes",
        4: "Vacuum house"
    }

    # get the task list and load it into a dict
    def load_json():
        pass

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
