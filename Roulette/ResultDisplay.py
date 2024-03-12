from Roulette import ColorThrow, RowSelector, ColumnSelector, EvenOddThrow, ThirdSelector
from Roulette.LogController import LogController


class ResultDisplay:

    @staticmethod
    def log(result: int):
        color_throw = ColorThrow.ColorThrow()
        rows_selector = RowSelector.RowSelector()
        even_throw_selector = EvenOddThrow.EvenOddThrow()
        column_selector = ColumnSelector.ColumnSelector()
        third_selector = ThirdSelector.ThirdSelector()

        LogController.display_header('Throw data')
        LogController.display('\tNumber:\t' + str(result))
        LogController.display('\tColor:\t' + color_throw.as_string(result))
        LogController.display('\tType:\t' + even_throw_selector.as_string(result))
        LogController.display('\tHalf:\t' + rows_selector.get_half_as_string(result))
        LogController.display('\tColumn:\t' + column_selector.as_string(result))
        LogController.display('\tThird:\t' + third_selector.get_third_as_string(result))
        LogController.display_header_end()
