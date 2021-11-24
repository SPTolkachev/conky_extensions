#!/usr/bin/env python3
import os
import argparse
import datetime as dt
from helpers.main import getDatetimeFromString
from helpers.main import getStrOfNumberWithLeadingZero
from helpers.text import translate
from helpers.animatetext import movingText


class DaysBefore():
    def __init__(self) -> None:
        self.parseArgs()

    def __repr__(self) -> str:
        return self.getStringOfRemainingDays()

    def parseArgs(self) -> None:
        parser = argparse.ArgumentParser(
            prog=os.path.basename(__file__),
            usage='%(prog)s [options]',
            description=(
                'Returns the number of days before the '
                'specified date (and time).'
            )
        )
        parser.add_argument(
            '-d',
            '--day',
            type=str,
            help='target day',
            required=True
        )
        parser.add_argument(
            '--hours',
            action='store_true',
            help='enable hours output'
        )
        parser.add_argument(
            '-m',
            '--minutes',
            action='store_true',
            help='enable minutes output'
        )
        parser.add_argument(
            '-s',
            '--seconds',
            action='store_true',
            help='enable seconds output'
        )
        parser.add_argument(
            '-et',
            '--event_text',
            type=str,
            help='the text that will be displayed after the event'
        )
        parser.add_argument(
            '-l',
            '--lang',
            type=str,
            help='language'
        )
        self.args = parser.parse_args()

        if self.args.seconds:
            self.args.hours = True
            self.args.minutes = True
        elif self.args.minutes:
            self.args.hours = True

    def getStringOfRemainingDays(self) -> str:
        remaining_time = self.getRemainingTimeData()

        text = ''
        if remaining_time['days'] >= 0:
            days = ''
            show_days = remaining_time['days'] > 0
            if show_days:
                days += str(remaining_time['days'])
                days += ' ' + translate('days', self.args.lang)
            else:
                self.args.hours = True
                self.args.minutes = True
                self.args.seconds = True

            time = ''
            if self.args.seconds or self.args.minutes or self.args.hours:
                time = self.getStringOfRemainingTime(remaining_time)

            text = (f'{days} {time}').strip()
        else:
            if self.args.event_text is None:
                text = translate('the event has come', self.args.lang)
            else:
                text = self.args.event_text
            text = movingText(text)

        return text

    def getRemainingTimeData(self) -> dict:
        target = getDatetimeFromString(self.args.day)
        now = dt.datetime.now()
        delta = target - now

        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        data = {
            'days': delta.days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
        }

        return data

    def getStringOfRemainingTime(self, remaining_time: dict) -> str:
        string = ''
        if self.args.hours:
            string += getStrOfNumberWithLeadingZero(remaining_time['hours'])
        if self.args.minutes:
            minutes = getStrOfNumberWithLeadingZero(remaining_time['minutes'])
            string += f':{minutes}'
        if self.args.seconds:
            seconds = getStrOfNumberWithLeadingZero(remaining_time['seconds'])
            string += f':{seconds}'

        return string


def main() -> None:
    days = DaysBefore()
    print(days)


if __name__ == '__main__':
    main()
