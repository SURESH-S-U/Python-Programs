def build(arr, l, r, i, tree):
    if l == r:
        tree[i] = arr[l]
        return arr[l]
    m = (l + r) // 2
    tree[i] = build(arr, l, m, 2 * i + 1, tree) + build(arr, m + 1, r, 2 * i + 2, tree)
    return tree[i]

def query(l, r, ql, qr, i, tree):
    if ql <= l and qr >= r:
        return tree[i]
    if qr < l or ql > r:
        return 0
    m = (l + r) // 2
    return query(l, m, ql, qr, 2 * i + 1, tree) + query(m + 1, r, ql, qr, 2 * i + 2, tree)

def update(l, r, idx, diff, i, tree):
    if idx < l or idx > r:
        return
    tree[i] += diff
    if l != r:
        m = (l + r) // 2
        update(l, m, idx, diff, 2 * i + 1, tree)
        update(m + 1, r, idx, diff, 2 * i + 2, tree)

def main():
    arr = list(map(int, input("Array: ").split()))
    n = len(arr)
    tree = [0] * (4 * n)

    build(arr, 0, n - 1, 0, tree)

    ql, qr = map(int, input("Query range (start end): ").split())
    print("Range sum:", query(0, n - 1, ql, qr, 0, tree))

    idx, new = map(int, input("Update index and new value: ").split())
    diff = new - arr[idx]
    arr[idx] = new
    update(0, n - 1, idx, diff, 0, tree)

    print("Tree after update:", tree)
    print("Updated range sum:", query(0, n - 1, ql, qr, 0, tree))

if __name__ == "__main__":
    main()