def make_readable(seconds):
    hour = seconds // (3600)
    sec = seconds % (3600)
    minutes = sec // 60
    seconds = seconds % 60

    return "%02d:%02d:%02d"  % (hour, minutes, seconds)
     