# --- INITIALIZATION ---
l1 = ['a', 'b']
print(f"l1 = {l1}, len of l1 = {len(l1)}")
print('-'*10)

# 1. append() - Adds an element to the end
l1.append('c')
print(f"l1 after append = {l1}, len of l1 = {len(l1)}")

# --- REFERENCE LOGIC (l2 = l1) ---
l2 = l1
print('-'*10)
print(f'l2 = l1 and then l2 = {l2}, len l2 = {len(l2)}')
print('-'*10)

# 2. clear() - Removes all elements (Affects both because they share memory)
l2.clear()
print(f'l2 after clear = {l2}, len l2 = {len(l2)}')
print(f'l1 after clear on l2 = {l1}, len l1 = {len(l1)}')

print('now we init value')
print()

# --- COPY LOGIC (l2 = l1.copy()) ---
l1 = ['arc', 'da25']
print(f"l1 = {l1}, len of l1 = {len(l1)}")
print('-'*10)

# 3. copy() - Creates a shallow copy (Independent memory)
l2 = l1.copy()
print(f"l2 = {l2}, len of l2 = {len(l2)}")
print('-'*10)

l2.clear()
print(f'l2 after clear = {l2}, len l2 = {len(l2)}')
print(f'l1 after clear on l2 = {l1}, len l1 = {len(l1)} (l1 retains values)')

# 4. append() with a list vs 5. extend()
l2.append(['a', 'c'])
print('-'*10)
print(f'l2 after append [a,c] as one item = {l2}, len l2 = {len(l2)}')

l2.clear()
print('-'*10)

l2.extend(['a', 'c'])
print(f'l2 after extend [a,c] as individual items = {l2}, len l2 = {len(l2)}')

# 6. insert() - Adds 'b' at index 1
l2.insert(1, 'b')
print('-'*10)
print(f'l2 after insert "b" at index 1 = {l2}, len l2 = {len(l2)}')

# 7. index() - Finds the position of a value
pos = l2.index('c')
print(f'Index of "c" in l2 = {pos}')

# 8. count() - Counts occurrences
l2.append('a')
print(f'l2 after adding another "a" = {l2}')
print(f'Count of "a" in l2 = {l2.count("a")}')

# 9. pop() - Removes and returns item at index (default last)
removed = l2.pop(1)
print(f'Popped item at index 1: {removed}, l2 now = {l2}')

# 10. remove() - Removes first occurrence of a value
l2.remove('a')
print(f'l2 after remove("a"): {l2}')

# 11. sort() & reverse()
l2.extend(['z', 'm'])
print(f'l2 before sort = {l2}')
l2.sort()
print(f'l2 after sort = {l2}')
l2.reverse()
print(f'l2 after reverse = {l2}')