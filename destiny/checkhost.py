def loop1():
    import os
    import time
    host = input("host:")
    os.system(f"""curl -H "Accept: application/json" \
  'https://check-host.net/check-ping?host={host}&max_nodes=3'""")
    time.sleep(10)


def loop2():
    while True:
        loop1()


loop2()
