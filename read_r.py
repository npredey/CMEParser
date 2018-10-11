import re
import fnmatch


path = "output2.txt"

# Gets element in form of i.e. "DEC19"
regex_date = '([a-zA-Z][a-zA-Z][a-zA-Z]\d\d)'

# Identifies a strike after a date i.e. "NOV18"
regex_strike = re.compile('^\d\d\d\d')

# Splits double spaces but not between parentheses
regex_split_no_parens = '[ ]{2,}(?![^()]*\))'

# Identifies the strikes of the calls i.e. 9384   ------  93.2322
regex_call_strike = '^\d{3,}'


regex_header_no_space = ' *({}) *'


def strip_header(header):
    return [str(x).strip() for x in header if x != '\n']


def get_header_element_index(header_list, header):
    for element in header_list:
        if re.search(regex_header_no_space.format(header), element):
            return header_list.index(element)


def align_call_row(header, row):
    header_list = header.split(',')
    # print(str(header_list))
    row_list = row.split(',')
    if "CAB" in str(row_list):
        print(row)
    # print(str(row_list))
    row_list_iter = iter(row_list)
    next(row_list_iter)
    for i in range(len(header_list)):
        header_col = header_list[i].strip()
        next_row_element = next(row_list_iter, 'DONE')
        # print(next_row_element)
        if "SETT.PRICE & PT.CHGE." in header_col:
            row_list[i] = row_list[i] + ' ' + next_row_element.strip()
            row_list.pop(i+1)
        elif "OPEN INTEREST" in header_col:
            print(next_row_element)
            split_next_element = next_row_element.split()
            print(split_next_element)
            oi = split_next_element[0]
            row_list[i] = row_list[i] + ' ' + oi
            row_list.insert(i+1, ' '.join(split_next_element[1:]))
    return ','.join(row_list)


def merge_headers(top_header, bottom_header, bottom_header_value='DISCOUNT % PT.CHGE.##', cols_to_skip=None):
    if cols_to_skip is None:
        cols_to_skip = ['DELTA']
    th_list = list(filter(None, re.split(' {2}', top_header)))
    bh_list = list(filter(None, re.split(' {2}', bottom_header)))

    merge_start_index = get_header_element_index(bh_list, bottom_header_value)
    merged_header = bh_list[:merge_start_index]
    top_index = 0
    for i in range(merge_start_index, len(bh_list)):
        element = bh_list[i].strip()
        if element in cols_to_skip:
            print(element)
            merged_header.append(element)
            continue
        if top_index != len(th_list):
            if element.strip() == "HIGH":
                header = "{} ({} {})".format(th_list[top_index], element, bh_list[-1])
            else:
                header = '{} {}'.format(th_list[top_index].strip(), element.strip())
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
    strike_call_file = open('strikes.csv', 'w+')
    for line in lines:
        if "EURO DOLLAR FUTURES" in line:
            ed_futures = True
            print(line)
            euro_dollar_headers = lines[i:i+3]
            print(euro_dollar_headers)
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
            stripped_ed_call_headers = strip_header(lines[i:i+3])
            print(stripped_ed_call_headers)
            options_headers = merge_headers(stripped_ed_call_headers[1], stripped_ed_call_headers[-1], '& PT.CHGE.')
            new_first = options_headers[0].split(' ')
            new_first[:1] = [' '.join(new_first[:1])]
            print(new_first)
            options_headers = ','.join([",".join(options_headers[0].split(' ')[0:])] + options_headers[1:])
            options_headers = options_headers.replace('OPEN,RANGE', 'OPEN RANGE')
            options_headers = ',,' + options_headers.replace('--CONTRACT--', 'CONTRACT ')
            strike_call_file.write(options_headers + '\n')
            ed_call_options = True
            ed_futures = False
        if ed_call_options:
            element = re.search(regex_date, line)
            call_strike = re.search(regex_call_strike, line)
            if element:
                futures_match = True
                strike_match_header = ','.join(re.split(regex_split_no_parens, line.strip()))
                # strike_call_file.write(strike_match_header + '\n')
                # strike_call_file.write(strike_match_header + '\n')
            elif call_strike:
                print(line)
                line = line.replace('-- --', '--  --')
                line = line.replace('---- ', '----  ')
                # print(re.sub(r'(\d)( ----)', r'\1 \2', line))
                print(line)
                call = strike_match_header + ',' + ','.join(re.split(regex_split_no_parens, line))
                print(call)
                call = align_call_row(options_headers, call)
                print(call)
                strike_call_file.write(call)

        i += 1
    f.close()
    strike_call_file.close()
