#  tableformat.py

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end='')
        print()
        print(('  ' + '-'*8)*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end='')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in csv format
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print('.'.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        print('<tr><th>', end='')
        print('</th><th>'.join(headers), end='')
        print('</th></tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')

def create_formatter(fmt: str):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    
def print_table(portfolio, headers, formatter):
    formatter.headings(headers)
    for stock in portfolio:
        rows = [str(getattr(stock, header)) for header in headers]
        formatter.row(rows)

