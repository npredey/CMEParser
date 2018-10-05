import re

path = "C:/Users/npredey/Desktop/output.txt"

# Gets element in form of i.e. "DEC19"
regex_date = '([a-zA-Z][a-zA-Z][a-zA-Z]\d\d)'

# Identifies a strike after a date i.e. "NOV18
regex_strike = re.compile('^\d\d\d\d')

# Splits double spaces but not between parentheses
regex_split_no_parens = '[  ]{2,}(?![^()]*\))'


def strip_header(header):
    return [str(x).strip() for x in header if x != '\n']


def merge_headers(top_header, bottom_header, bottom_header_value='DISCOUNT % PT.CHGE.##', cols_to_skip=None):
    if cols_to_skip is None:
        cols_to_skip = ['DELTA']
    th_list = list(filter(None, re.split('  +', top_header)))
    bh_list = re.split('  +', bottom_header)
    merge_start_index = bh_list.index(bottom_header_value)
    merged_header = bh_list[:merge_start_index]
    top_index = 0
    for i in range(merge_start_index, len(bh_list)):
        element = bh_list[i]
        if element in cols_to_skip:
            continue
        if top_index != len(th_list):
            if element == "HIGH":
                header = "{} ({} {})".format(th_list[top_index], element, bh_list[-1])
            else:
                header = '{} {}'.format(th_list[top_index], element)
            merged_header.append(header)
            top_index += 1
    return merged_header


def main():
    f = open(path, 'r')
    lines = f.readlines()

    i = 0
    futures_headers = list()
    ed_call_options = False
    ed_futures = False
    futures_match = False
    strike_match_header = ''

    for line in lines:
        if "EURO DOLLAR FUTURES" in line:
            ed_futures = True
            # print(line)
            euro_dollar_headers = lines[i:i+5]
            # print(euro_dollar_headers)
            euro_dollar_headers = [str(x).strip() for x in euro_dollar_headers if x != '\n']
            futures_headers = merge_headers(euro_dollar_headers[1], euro_dollar_headers[-1])
        if ed_futures:
            element = re.search(regex_date, line)
            if element:
                futures_match = True
                print(re.split(regex_split_no_parens, line))

        else:
            futures_match = False

        if 'EURODOLLAR CALLS' in line:
            print(line)
            print("EURODOLLAR CALLS")
            stripped_ed_call_headers = strip_header(lines[i:i+5])
            print(stripped_ed_call_headers)
            options_headers = merge_headers(stripped_ed_call_headers[1], stripped_ed_call_headers[-1], '& PT.CHGE.')
            new_first[1:] = [" ".join(q[1:])]
            options_headers = [" ".join(options_headers[0].split(' ')[1:])] + options_headers[1:]
            print(options_headers)
            ed_call_options = True
            ed_futures = False
        if ed_call_options:
            element = re.search(regex_date, line)
            if element:
                futures_match = True
                print(re.split(regex_split_no_parens, line))

        i += 1
    f.close()


main()
