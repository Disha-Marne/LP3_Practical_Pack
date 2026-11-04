"""Practical 4: N-Queens using Backtracking with first Queen placed."""

def solve_n_queens(n, first_row, first_col):

    if n < 1:
        return None

    if not (0 <= first_row < n and 0 <= first_col < n):
        return None

    board = [['.'] * n for _ in range(n)]

    # Place the first queen
    board[first_row][first_col] = 'Q'

    columns = {first_col}
    diag1 = {first_row - first_col}
    diag2 = {first_row + first_col}

    def backtrack(row):

        if row == n:
            return True

        # Skip the row containing the first queen
        if row == first_row:
            return backtrack(row + 1)

        for col in range(n):

            d1 = row - col
            d2 = row + col

            if col in columns or d1 in diag1 or d2 in diag2:
                continue

            board[row][col] = 'Q'
            columns.add(col)
            diag1.add(d1)
            diag2.add(d2)

            if backtrack(row + 1):
                return True

            # Backtracking
            board[row][col] = '.'
            columns.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)

        return False

    return board if backtrack(0) else None


def main():
    try:
        n = int(input("Enter N: "))
        first_row = int(input("Enter first queen row (0-based): "))
        first_col = int(input("Enter first queen column (0-based): "))
    except ValueError:
        print("Invalid input.")
        return

    solution = solve_n_queens(n, first_row, first_col)

    if solution is None:
        print("No solution exists for this initial position.")
    else:
        print("N-Queens Solution:")
        for row in solution:
            print(' '.join(row))


if __name__ == '__main__':
    main()
