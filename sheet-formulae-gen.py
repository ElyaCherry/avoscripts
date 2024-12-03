"""
This file lacks
if __name__ == "__main__":
and was written with no regard for:
 - potential usage by someone else besides the author,
 - code readability,
 - showcasing my skills, etc.
"""


def put_isnumber(col: str):
    return f"IF(ISNUMBER('Form Responses 1'!{col}2:{col}), 'Form Responses 1'!{col}$1, \"\")"


def put_number(col: str):
    return f"'Form Responses 1'!{col}2:{col}"


def assemble_text(range_: str):
    cols = range_.rstrip().split()
    return " & ".join([put_isnumber(col) for col in cols])


def assemble_num(range_: str):
    cols = range_.rstrip().split()
    return " + ".join([put_number(col) for col in cols])


def assemble_all(range_: str):
    return assemble_text(range_) + ' \n & ": " & CHAR(10) & \n (' + assemble_num(range_) + ')'


def make_array(formula: str):
    return "=ARRAYFORMULA(IFERROR( \n" + formula + "\n , \"\"))"


ranges = [
    "P AC AO BA BN CA CP DC EB EN EZ FL FX GJ GV HH HT IG IU JH JU KH KV LH LU MH",  #1
    "Q AD AP BB BO CB CQ DD EC EO FA FM FY GK GW HI HU IH IV JI JV KI KW LI LV MI",  #2
    "R AE AQ BC BP CC CR DE ED EP FB FN FZ GL GX HJ HV II IW JJ JW KJ KX LJ LW MJ",  #3
    "S AF AR BD BQ CD CS DF EE EQ FC FO GA GM GY HK HW IJ IX JK JX KK KY LK LX MK",  #4
    "T AG AS BE BR CE CT DG EF ER FD FP GB GN GZ HL HX IK IY JL JY KL KZ LL LY ML",  #5
    "U AH AT BF BS CF CU DH EG ES FE FQ GC GO HA HM HY IL IZ JM JZ KM LA LM LZ MM",  #6
    "V AI AU BG BT CG CV DI EH ET FF FR GD GP HB HN HZ IM JA JN KA KN LB LN MA MN",  #7
    "W AJ AV BH BU CH CW DJ EI EU FG FS GE GQ HC HO IA IN JB JO KB KO LC LO MB MO",  #8
    "X AK AW BI BV CI CX DK EJ EV FH FT GF GR HD HP IB IO JC JP KC KP LD LP MC MP",  #9
    "Y BJ BW CJ CY DL EK EW FI FU GG GS HE HQ IC IP JD JQ KD KQ LQ MD MQ",           #10
    "CK",  #11
    "CL"   #12
]

for range_ in ranges:
    #print(make_array(assemble_all(range_)), end='\n\n\n')
    #print(make_array(assemble_text(range_)), end='\n\n')
    #print(make_array(assemble_num(range_)), end='\n\n\n\n')
    pass

new_ranges = [
    "IU JH JU KH KV LH LU MH",  #1
    "IV JI JV KI KW LI LV MI",  #2
    "IW JJ JW KJ KX LJ LW MJ",  #3
    "IX JK JX KK KY LK LX MK",  #4
    "IY JL JY KL KZ LL LY ML",  #5
    "IZ JM JZ KM LA LM LZ MM",  #6
    "JA JN KA KN LB LN MA MN",  #7
    "JB JO KB KO LC LO MB MO",  #8
    "JC JP KC KP LD LP MC MP",  #9
    "JD JQ KD KQ LQ MD MQ",     #10
]

additional_ranges = [
    "JE JR KE KR LE LR ME MR",  # общие моменты
    "JF JS KF KS LF LS MF MS",  # комментарии
    "IT JG JT KG KU LG LT MG"  # решали ли пробный тест
]


def add_range_to_additional(range_: str):
    res = '\n'
    for col in range_.split():
        res += f"  IF(ISTEXT('Form Responses 1'!{col}2:{col}), 'Form Responses 1'!{col}2:{col}, \n"
    return res


def add_range_to_tasks_texts(range_: str):
    res = '\n'
    for col in range_.split():
        res += f" & IF(ISNUMBER('Form Responses 1'!{col}2:{col}), 'Form Responses 1'!{col}$1, \"\")"
    return res


def add_range_to_tasks_marks(range_: str):
    res = '\n'
    for col in range_.split():
        res += f" + 'Form Responses 1'!{col}2:{col}"
    return res


for range_ in new_ranges:
    print(add_range_to_tasks_texts(range_))
    print('\n\n')

print('\n\n')

for range_ in new_ranges:
    print(add_range_to_tasks_marks(range_))
    print('\n\n')

print('\n\n\n')

for range_ in additional_ranges:
    print(add_range_to_additional(range_))
    print('\n\n')
