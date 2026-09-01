class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])
        litter = {}
        start = None
        idx = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = idx
                    idx += 1
        total_litter = idx
        final_mask = (1 << total_litter) - 1
        if final_mask == 0:
            return 0
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))
        best = {(start[0], start[1], 0): energy}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, mask, curr_energy, moves = q.popleft()
            if curr_energy == 0:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                new_energy = curr_energy - 1
                new_mask = mask
                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)
                if classroom[nr][nc] == 'R':
                    new_energy = energy
                if new_mask == final_mask:
                    return moves + 1
                state = (nr, nc, new_mask)
                if state in best and best[state] >= new_energy:
                    continue
                best[state] = new_energy
                q.append((nr, nc, new_mask, new_energy, moves + 1))
        return -1   
        