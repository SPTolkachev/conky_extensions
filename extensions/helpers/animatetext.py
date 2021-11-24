import time


def movingText(
        text: str,
        speed: int = 1,
        space: int = 3
        ) -> str:
    if speed <= 0:
        raise ValueError(
            'movingText: '
            f'the speed value ({speed}) must be greater than or equal to zero'
        )
    if space <= 0:
        raise ValueError(
            'movingText: '
            f'the space value ({space}) must be greater than or equal to zero'
        )

    text += ' ' * space
    unixtime = int(time.time())
    len_text = len(text)
    offset = unixtime % len_text
    offset = (offset * speed) % len_text
    return text[offset:] + text[:offset]
