import json

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)

    except FileNotFoundError:
        tasks = []

    return tasks


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


import json


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

    return tasks


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("暂无任务")
    else:
        for i in range(0, len(tasks)):
            print(i + 1, tasks[i])


def add_task(tasks):
    name = input("输入任务：")
    tasks.append(name)
    print("添加成功")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== Todo List =====")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 退出")

        choice = input("请选择：")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            break


if __name__ == "__main__":
    main()
    




    
