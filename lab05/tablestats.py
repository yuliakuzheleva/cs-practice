def read_rows(lines):
    rows = []
    name = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = line.split(",")
        for i in range(len(fields)):
            fields[i] = fields[i].strip()
        if header is None:
            name = fields
            continue
        row = {}
        for i in range(len(name)):
            row[name[i]] = fields[i]
        row.append(row)
    return rows
