import datetime as dt
import re


def getStrOfNumberWithLeadingZero(num: int) -> str:
    result = ''

    if num >= 0:
        if num < 10:
            result = f'0{num}'
        else:
            result = str(num)
    else:
        raise ValueError(
            'getStrOfNumberWithLeadingZero: '
            f'the number ({num}) must be greater than or equal to zero'
        )

    return result


def getDatetimeFromString(day: str) -> dt.datetime:
    r_hour = r'(?P<hour>\d{1,2})'
    r_minute = r'(?P<minute>\d{1,2})'
    r_second = r'(?P<second>\d{1,2})'
    match = re.match(
        (
            r'(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)'
            r'( ' + r_hour + r'(:' + r_minute + r'(:' + r_second + r')?)?)?'
        ),
        day,
        flags=re.I
    )

    if match is None:
        raise ValueError(
            'getDatetimeFromString: '
            f'the date ({day}) must be in the format YYYY-MM-DD [hh[:mm[:ss]]]'
        )

    data = match.groupdict()
    hour = 0 if data['hour'] is None else data['hour']
    minute = 0 if data['minute'] is None else data['minute']
    second = 0 if data['second'] is None else data['second']

    return dt.datetime(
        year=int(data['year']),
        month=int(data['month']),
        day=int(data['day']),
        hour=int(hour),
        minute=int(minute),
        second=int(second)
    )
