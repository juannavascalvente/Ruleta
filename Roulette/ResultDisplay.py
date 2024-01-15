from Roulette import ColorThrow, RowSelector, ColumnSelector, EvenOddThrow, ThirdSelector


class ResultDisplay:

    @staticmethod
    def display(result: int):
        color_throw = ColorThrow.ColorThrow()
        rows_selector = RowSelector.RowSelector()
        even_throw_selector = EvenOddThrow.EvenOddThrow()
        column_selector = ColumnSelector.ColumnSelector()
        third_selector = ThirdSelector.ThirdSelector()

        print('----------------------------- Throw data ----------------------------------')
        print('\tNumber:\t' + str(result))
        print('\tColor:\t' + color_throw.as_string(result))
        print('\tType:\t' + even_throw_selector.as_string(result))
        print('\tHalf:\t' + rows_selector.get_half_as_string(result))
        print('\tColumn:\t' + column_selector.as_string(result))
        print('\tThird:\t' + third_selector.get_third_as_string(result))
        print('---------------------------------------------------------------------------')

    @staticmethod
    def write(f, result: int):
        color_throw = ColorThrow.ColorThrow()
        rows_selector = RowSelector.RowSelector()
        even_throw_selector = EvenOddThrow.EvenOddThrow()
        third_selector = ThirdSelector.ThirdSelector()
        column_selector = ColumnSelector.ColumnSelector()

        f.write('\tNumber:\t' + str(result) + '\n')
        f.write('\tColor:\t' + color_throw.as_string(result) + '\n')
        f.write('\tType:\t' + even_throw_selector.as_string(result) + '\n')
        f.write('\tHalf:\t' + rows_selector.get_half_as_string(result) + '\n')
        f.write('\tColumn:\t' + column_selector.as_string(result) + '\n')
        f.write('\tThird:\t' + third_selector.get_third_as_string(result) + '\n')
