# здесь я поключу базу данных
def add_tasks(task):
    import sqlite3
    con = sqlite3.connect("db/completed_tasks.db")
    cur = con.cursor()
    results1 = cur.execute("INSERT INTO complected_tasks (name) VALUES (?)", (task[3:],))
    con.commit()
    con.close()
    con = sqlite3.connect("db/completed_tasks.db")
    cur = con.cursor()
    results2 = cur.execute("SELECT name FROM complected_tasks ORDER BY id DESC LIMIT 10").fetchall()
    con.close()
    return [result[0] for result in results2]


if __name__ == '__main__':
    add_tasks(input())
