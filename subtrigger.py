def run_echo():
    from subprocess import Popen, PIPE

    p = Popen(["echo", "Hello, world!"], stdout=PIPE)
    return p.communicate()[0]
