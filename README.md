# tasks-cli
A basic CLI task management tool

## Installing
To install, clone the repository and navigate to the root of
the project (where setup.py is located).

Then run
```
pip install .
```

Now run 
```
tasks-cli
```

# help page
```
A simple and minimalistic CLI tool to track tasks!

usage: tasks-cli [option] [id | descr | status] [descr]

Options:
add (descr)             : Takes a (descr)iption of the task as a string
update (id) (descr)     : Takes a task (id) as an integer, then a task (descr)iption as a string
list [status]           : Takes an optional string for the status, defaults to showing all tasks.
                          Status can be one of the following: todo, done, in-progress

Detailed man page coming soon.
```
