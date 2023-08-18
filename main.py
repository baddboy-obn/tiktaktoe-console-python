# Инициализация пустого игрового поля
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отрисовки игрового поля
def draw_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Функция для проверки условия победы
def check_win(board, player):
    # Проверка по горизонтали и вертикали
    for i in range(3):
        if all(mark == player for mark in board[i]) or all(mark == player for mark in [board[j][i] for j in range(3)]):
            return True
    # Проверка по диагоналям
    if all(mark == player for mark in [board[i][i] for i in range(3)]) or all(mark == player for mark in [board[i][2-i] for i in range(3)]):
        return True
    return False

# Основной игровой цикл
def main():
    current_player = 'X'  # Задаем текущего игрока

    while True:
        draw_board(board)  # Отрисовываем игровое поле
        row = int(input('Введите номер строки (от 1 до 3): ')) - 1
        col = int(input('Введите номер столбца (от 1 до 3): ')) - 1

        # Проверка на корректность ввода координат
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print('Неверные координаты. Попробуйте снова.')
            continue

        board[row][col] = current_player  # Заполняем ячейку игрового поля

        # Проверка на победу или ничью
        if check_win(board, current_player):
            print('Игрок', current_player, 'выиграл!')
            break
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print('Ничья!')
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()