import gspread
from gspread.utils import rowcol_to_a1


class GoogleSheetsUpdater:
    def __init__(self, spreadsheet_name, worksheet_name, header=3, offset=4, problem_row=1):
        self.problem_row = problem_row
        self.gc = gspread.service_account()
        self.gs = self.gc.open(spreadsheet_name)
        self.wks = self.gs.worksheets()[[i.title for i in self.gs.worksheets()].index(worksheet_name)]

        self.header = header
        self.offset = offset

    def get_students_list(self):
        students = self.wks.get(f'A{self.header + 1}:A')
        return list(map(lambda x: x[0], students[:students.index([])]))

    def update_sheet(self, standings):
        self.wks.update(rowcol_to_a1(1, self.offset + 1), standings.name)
        self.wks.update(
            rowcol_to_a1(self.header + 1, self.offset + 1) + ":" +
            rowcol_to_a1(self.header + len(standings.results),
                         self.offset + max(len(row) for row in standings.results)),
            standings.results)
        self.offset += len(standings.problems)
