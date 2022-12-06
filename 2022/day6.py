def find_marker(char_stream, marker_length):
    count = 0
    buffer = []
    for l in line:
        buffer.append(l)
        count += 1
        if len(buffer) == marker_length:
            if len(set(buffer)) == marker_length:
                return count
            else:
                buffer.pop(0)
    
    return -1

with open('input/day6.txt') as f:
    line = f.readline().strip()

    print(f"Start-of-packet marker found after {find_marker(line, 4)} characters received")
    print(f"Start-of-message marker found after {find_marker(line, 14)} characters received")
