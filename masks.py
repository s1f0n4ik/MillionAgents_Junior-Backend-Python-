class EmailMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char

    def mask(self, email):
        local_part, domain = email.split('@')
        masked_local_part = self.mask_char * len(local_part)
        return f"{masked_local_part}@{domain}"


class PhoneNumberMasker:
    def __init__(self, mask_char='x', num_chars_to_mask=3):
        self.mask_char = mask_char
        self.num_chars_to_mask = num_chars_to_mask

    def mask(self, phone_number):
        # Убираем лишние пробелы
        phone_number = ' '.join(phone_number.split())

        # Оставляем только последние 'num_chars_to_mask'
        numbers_part = phone_number.replace(' ', '')[:-self.num_chars_to_mask]
        masked_part = self.mask_char * self.num_chars_to_mask

        result = ''
        i, j = 0, 0
        for char in phone_number:
            if char == ' ':
                result += ' '
            else:
                if i < len(numbers_part):
                    result += numbers_part[i]
                    i += 1
                else:
                    result += masked_part[j]
                    j += 1
        return result


class SkypeMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char

    def mask(self, skype_handle):
        if skype_handle.startswith("skype:"):
            if '<a href="' in skype_handle:
                return self._mask_link(skype_handle)
            else:
                return self._mask_handle(skype_handle)
        return skype_handle

    # aboba
    def _mask_handle(self, handle):
        new_handle = "skype:" + self.mask_char * 3
        return new_handle

    def _mask_link(self, link):
        parts = link.split('"')
        handle_part = parts[1].split(':')
        new_link = link.replace(handle_part[1], self.mask_char * 3)
        return new_link

