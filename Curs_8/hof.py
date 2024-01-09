def to_file(event):
    with open("log.txt", "a") as f:
        f.write(f"{event}\n")

def write_log(event, logger_func=print):
    logger_func(event)


write_log("S-a intamplat ceva")
write_log("S-a intampla altceva", logger_func=to_file)