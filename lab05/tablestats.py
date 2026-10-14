def read_rows(lines):
    rows = []
    name = None
    for line in lines:
        line = line.strip(
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
def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind]=0
        counts[kind]+=1
    return counts
def to_csv(counts):
    res = ["тип, количество"]
    for kind in sorted(counts):
        lines.append(f"{kind}, {counts[kind]}")
    return "\n".join(res) + "\n"
